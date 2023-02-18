## generate dummy mardown content.
## This is a script to generate dummy content for testing purposes.


import datetime
import os
import random

# generate array of different technology stack tags.

def generate_tags():
	technology = ['react', 'angular', 'vue', 'node', 'java', 'python', 'php', 'c++', 'c#', 'ts']
	frameworks = ['gatsby', 'next', 'nuxt', 'nest', 'express', 'spring', 'django', 'laravel', 'flask', 'codeigniter']
	platforms = ['aws', 'firebase', 'heroku', 'docker', 'kubernetes', 'jenkins']
	databases = ['mongodb', 'mysql', 'postgresql', 'sqlite', 'oracle', 'mssql']
	cloud = ['azure', 'gcp']
	tools = ['git', 'github', 'gitlab', 'bitbucket', 'jira', 'trello', 'slack', 'notion']
	testing = ['jest', 'mocha', 'chai', 'jasmine', 'cypress', 'selenium']
	programming = ['c', 'c++', 'c#', 'java', 'python', 'php', 'ts']
	other = ['pro', 'free', 'beginner', 'intermediate', 'advanced', 'expert', 'premium', 'pro', 'free']

	## generate random tags.
	tags = [ technology[random.randint(0, len(technology) - 1)], frameworks[random.randint(0, len(frameworks) - 1)], platforms[random.randint(0, len(platforms) - 1)], databases[random.randint(0, len(databases) - 1)], cloud[random.randint(0, len(cloud) - 1)], tools[random.randint(0, len(tools) - 1)], testing[random.randint(0, len(testing) - 1)], programming[random.randint(0, len(programming) - 1)], other[random.randint(0, len(other) - 1)] ]

	# tags = technology + frameworks + platforms + databases + cloud + tools + testing + programming + other

	return tags 


# generate dummy mardown content.
# This is a script to generate dummy content for testing purposes.


# generate array of different technology stack tags.


def generate_tags():
	technology = ['react', 'angular', 'vue', 'node',
               'java', 'python', 'php', 'c++', 'c#', 'ts']
	frameworks = ['gatsby', 'next', 'nuxt', 'nest', 'express',
               'spring', 'django', 'laravel', 'flask', 'codeigniter']
	platforms = ['aws', 'firebase', 'heroku', 'docker', 'kubernetes', 'jenkins']
	databases = ['mongodb', 'mysql', 'postgresql', 'sqlite', 'oracle', 'mssql']
	cloud = ['azure', 'gcp']
	tools = ['git', 'github', 'gitlab', 'bitbucket',
          'jira', 'trello', 'slack', 'notion']
	testing = ['jest', 'mocha', 'chai', 'jasmine', 'cypress', 'selenium']
	programming = ['c', 'c++', 'c#', 'java', 'python', 'php', 'ts']
	other = ['pro', 'free', 'beginner', 'intermediate',
          'advanced', 'expert', 'premium', 'pro', 'free']

	# generate random tags.
	tags = [technology[random.randint(0, len(technology) - 1)], frameworks[random.randint(0, len(frameworks) - 1)], platforms[random.randint(0, len(platforms) - 1)], databases[random.randint(0, len(databases) - 1)], cloud[random.randint(
		0, len(cloud) - 1)], tools[random.randint(0, len(tools) - 1)], testing[random.randint(0, len(testing) - 1)], programming[random.randint(0, len(programming) - 1)], other[random.randint(0, len(other) - 1)]]

	# tags = technology + frameworks + platforms + databases + cloud + tools + testing + programming + other

	return tags


def generate_content(count=100):
	for i in range(1, count):
		# create folder.
		# array of emogi unicode.
		emogi = [ '🫣', '👀', '😵‍💫',  '🤯', '🤗', '🤔', '🤓', '🤠', '🤑', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠', '🤡', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠', '🤡', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠', '🤡', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠', '🤡', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮', '🤢', '🤧', '🥵', '🥶', '🥴', '🤯', '🤠', '🤡', '🤥', '🤫', '🤭', '🤫', '🤪', '🤩', '🥳', '🤬', '🤮']

		
		folder_name = "course-" + str(i)
		os.mkdir(folder_name)

		file_name = '_index' + ".md"
		file_path = os.path.join(folder_name, file_name)
		with open(file_path, "w", encoding="utf-8") as f:
			f.write("---\n")
			# current time.
			f.write("lastmod: " + str(datetime.datetime.now()) + "\n")
			f.write("title: " + "Course " + str(i) + "\n")
			f.write("description: " + "Course " + str(i) + "\n")
			# random integer between 1 and 100.
			f.write("weight: " + str(random.randint(1, 100)) + "\n")
			# random emogi unicode.
			f.write("emogi: " + emogi[random.randint(0, len(emogi) - 1)] + "\n")
			f.write("type: courses\n")
			# add random tags.
			f.write("tags: \n")
			tags = generate_tags()
			for tag in tags:
				f.write("    - " + tag + "\n")

			f.write("\n")
			f.write("author: Akash Aman\n")
			f.write("---\n")

		# generate random number of chapters.

		for j in range(1, 40):
			chapter_name = "chapter-" + str(j) + ".md"
			chapter_path = os.path.join(folder_name, chapter_name)
			with open(chapter_path, "w", encoding="utf-8") as f:
				f.write("---\n")
				f.write("title: " + "Chapter " + str(j) + "\n")
				f.write("description: " + "Chapter " + str(j) + "\n")
				f.write("weight: " + str(random.randint(1, 100)) + "\n")
				f.write("emogi: " + emogi[random.randint(0, len(emogi) - 1)] + "\n")
				f.write("type: chapters\n")
				# chapter.
				f.write("chapter: " + str(j) + "\n")
				# add random section name.

				if j == 1 or random.randint(0, 2) == 1 :
					f.write("section_start: " + "Section " + str(j) + "\n")
					f.write("section_emogi: " + emogi[random.randint(0, len(emogi) - 1)] + "\n")


				f.write("---\n")
				f.write("\n")
				f.write("# Chapter " + str(j) + "\n")
				f.write("\n")
				# generate random number of lessons.

				for k in range(1, 10):
					f.write("## Lesson " + str(k) + "\n")
					f.write("\n")
					# generate random number of paragraphs.
					paragraph_count = random.randint(1, 10)
					for l in range(1, paragraph_count):
						f.write("Paragraph " + str(l) + "\n")
						f.write("\n")
						f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tincidunt, felis eget tincidunt scelerisque, elit neque vestibulum nisl, a varius ligula risus ut mi. Donec euismod, risus eget consectetur dapibus, erat lectus vulputate velit, et tempor turpis libero vel ante. Nulla facilisi. Nullam sed semper dolor. Praesent auctor, justo a suscipit aliquet, tellus enim sagittis tellus, non cursus felis urna eget nulla. Nullam vel felis vitae neque congue aliquam. Fusce id mauris vitae urna rhoncus congue. Sed pulvinar, nunc vitae imperdiet suscipit, turpis metus laoreet erat, nec fringilla ex enim nec massa. Nullam sed semper dolor. Praesent auctor, justo a suscipit aliquet, tellus enim sagittis tellus, non cursus felis urna eget nulla. Nullam vel felis vitae neque congue aliquam. Fusce id mauris")



def delete_content(count = 100):
	## delete all files from directory.
	for i in range(1, count):
		folder_name = "course-" + str(i)
		file_name = '_index' + ".md"
		file_path = os.path.join(folder_name, file_name)

		os.remove(file_path)
		## delete random no of chapters.
		chapter_count = random.randint(1, 10)
		for j in range(1, 40):
			chapter_name = "chapter-" + str(j) + ".md"
			chapter_path = os.path.join(folder_name, chapter_name)
			os.remove(chapter_path)
		
		os.rmdir(folder_name)

if __name__ == "__main__":
	print("For generation content press 1")
	print("For deleting content press 2")
	choice = int(input())
	count = 20
	if choice == 1:
		generate_content(count)
	else:
		delete_content(count)


		
## write emogi in a file.
