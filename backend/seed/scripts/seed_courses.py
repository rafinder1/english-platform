import json
from pathlib import Path

from apps.courses.models import Course, Lesson
from apps.content.models import Section, ContentBlock

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "business_english_b1.json"


def run():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Starting seed...")

    for course_id, course_data in data.items():

        # -------------------------
        # 1. COURSE
        # -------------------------
        course, _ = Course.objects.get_or_create(
            title=course_data["course_name"],
            slug=course_data["course_name"].lower().replace(" ", "-"),
        )

        print(f"Course: {course.title}")

        # -------------------------
        # 2. LESSONS
        # -------------------------
        for lesson_index, lesson_data in enumerate(
            course_data["lessons"], start=1
        ):

            lesson, _ = Lesson.objects.get_or_create(
                course=course,
                title=lesson_data["lesson_title"],
                order=lesson_index,
            )

            print(f"  Lesson: {lesson.title}")

            # -------------------------
            # 3. SECTIONS
            # -------------------------
            for section_index, section_data in enumerate(
                lesson_data["sections"], start=1
            ):

                section, _ = Section.objects.get_or_create(
                    lesson=lesson,
                    title=f"Section {section_index}",
                    type="main",
                    order=section_index,
                )

                print(f"    Section: {section.id}")

                # -------------------------
                # 4. CONTENT BLOCKS
                # -------------------------

                # opcjonalnie: żeby nie duplikować bloków
                section.blocks.all().delete()

                for block_index, block in enumerate(
                    section_data["content"], start=1
                ):

                    if block["type"] == "text":
                        block_data = {"text": block["text"]}

                    elif block["type"] == "heading":
                        block_data = {"text": block["text"]}

                    elif block["type"] == "image":
                        block_data = {
                            "url": block["source_url"],
                            "local_path": block.get("local_path"),
                        }

                    elif block["type"] == "list":
                        block_data = {"items": block["items"]}

                    else:
                        block_data = block

                    ContentBlock.objects.create(
                        section=section,
                        type=block["type"],
                        order=block_index,
                        data=block_data,
                    )

                print(f"      Blocks: {section.blocks.count()}")

    print("Seed completed.")