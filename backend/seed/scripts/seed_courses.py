import json
from pathlib import Path

from apps.courses.models import Course, Lesson
from apps.content.models import Section, ContentBlock

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "business_english_b1.json"


def run():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    for course_id, course_data in data.items():

        # 1. COURSE
        course, _ = Course.objects.get_or_create(
            title=course_data["course_name"],
            slug=course_data["course_name"].lower().replace(" ", "-"),
        )

        print(f"Created course: {course.title}")

        # 2. LESSONS
        for lesson_index, lesson_data in enumerate(course_data["lessons"], start=1):

            lesson, _ = Lesson.objects.get_or_create(
                course=course, title=lesson_data["lesson_title"], order=lesson_index
            )

            print(f"  Created lesson: {lesson.title}")

            # 3. SECTIONS
            for section_index, section_data in enumerate(
                lesson_data["sections"], start=1
            ):

                section = Section.objects.create(
                    lesson=lesson,
                    title=f"Section {section_index}",
                    type="main",
                    order=section_index,
                )

                print(f"    Created section {section.id}")

                # 4. CONTENT BLOCKS
                for block_index, block in enumerate(section_data["content"], start=1):

                    if block["type"] == "text":
                        data = {"text": block["text"]}

                    elif block["type"] == "heading":
                        data = {"text": block["text"]}

                    elif block["type"] == "image":
                        data = {
                            "url": block["source_url"],
                            "local_path": block.get("local_path"),
                        }

                    elif block["type"] == "list":
                        data = {"items": block["items"]}

                    else:
                        data = block

                    ContentBlock.objects.create(
                        section=section,
                        type=block["type"],
                        order=block_index,
                        data=data,
                    )

                print(f"      Created blocks for section")
