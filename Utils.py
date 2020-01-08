import json
import matplotlib.pyplot as plt
from collections import Counter


class Utils:
    # save scrapped articles in json file
    @classmethod
    def save_to_file(cls, articles):
        articles_list = []

        # add articles as dictionaries in a list
        for article in articles:
            articles_list.append({
                'name': article.get_title(),
                'author': article.get_author(),
                'url': article.get_url(),
                'tags': article.get_tags()
            })

        file = open('articles1.json', 'w')
        json.dump(articles_list, file, indent=4)
        file.close()

    @classmethod
    def read_file(cls, filename):
        try:
            file = open(filename, 'r')
            data = json.load(file)
            file.close()
            return data
        except FileNotFoundError:
            print('file not found')

    @classmethod
    def plot_graph(cls, x_axis, y_axis, x_axis_labels, plot_title):
        # set window size in which plot is drawn
        plt.figure(figsize=(10, 5))
        # plot the graph
        plt.bar(x_axis, y_axis, tick_label=x_axis_labels, width=0.5, color=['blue'])
        # name x-axis
        plt.xlabel('x - axis')
        # name y-axis
        plt.ylabel('y - axis')
        plt.title(plot_title)

    @classmethod
    def plot_related_tags(cls, most_used_tag, tag_lists):
        related_tag_frequency = {}

        for tag_list in tag_lists:
            if most_used_tag in tag_list:
                for t in tag_list:
                    if t in related_tag_frequency:
                        related_tag_frequency[t] += 1
                    else:
                        related_tag_frequency[t] = 1

        most_used_tag_frequency = related_tag_frequency[most_used_tag]
        confidence = 40
        min_related_frequency = (most_used_tag_frequency * confidence) / 100

        related_tags = []

        for key, value in related_tag_frequency.items():
            if value >= min_related_frequency and key != most_used_tag:
                related_tags.append((key, value))

        if len(related_tags) == 0:
            print('no related tags with atleast 40% confidence exist for most used tag')
            return

        x_axis = [i for i in range(len(related_tags))]
        y_axis = []
        x_axis_labels = []

        for t in related_tags:
            x_axis_labels.append(t[0])
            y_axis.append(t[1])

        Utils.plot_graph(x_axis, y_axis, x_axis_labels, 'Related Tags')

    @classmethod
    def plot_most_used_tags(cls, most_used_tags):
        # x-coordinates
        x_axis = [1, 2, 3, 4, 5]
        # y-coordinates
        y_axis = []
        x_axis_labels = []

        # fill y-coordinates list and x-axis labels list
        for tag in most_used_tags:
            x_axis_labels.append(tag[0])
            y_axis.append(tag[1])

        Utils.plot_graph(x_axis, y_axis, x_axis_labels, 'Top Issues in Current Affairs')

    @classmethod
    def draw_charts(cls, filename):
        # read file containing data about articles
        articles_list = Utils.read_file(filename)

        # will contains all tags merged in a single list
        # used to plot most used tags
        tags = []
        # will contain lists of tags
        # used to plot related tags
        tag_lists = []

        # extract tags of from each article and merge each tag list in to one list
        # also fill tags_lists
        for article in articles_list:
            tags.extend(article['tags'])
            tag_lists.append(article['tags'])

        # get 5 most occurring tags  and their frequency in descending order
        # e.g. [('Middle East, 4), ('Iran', 3)]
        most_used_tags = [(tag, tag_count) for tag, tag_count in Counter(tags).most_common(5)]

        Utils.plot_most_used_tags(most_used_tags)
        # first item of the first tuple in most_used_tags list is the most
        # frequent tag
        most_frequent_tag = most_used_tags[0][0]
        Utils.plot_related_tags(most_frequent_tag, tag_lists)

        # show all plot figures at the same time
        plt.show()
