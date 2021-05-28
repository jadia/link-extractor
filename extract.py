#!/usr/bin/python3.8
from typing import List
from bs4 import BeautifulSoup
import requests
import argparse


class GetFileLinks():
    """Get direct links of all the files with a specific extension on the HTML
    page.
    """
    def __init__(self, url, ext) -> None:
        self.url = url
        self.ext = ext

    def get_file_links(self) -> List:
        """Extract links from webpage and return list of URL with the provided
        extension.

        Args:
            url ([str]): URL to a webpage
            ext ([str]): extension of files whose direct links need to be
            extracted from the provided URL

        Returns:
            List: List of URL with extension
        """
        try:
            page = requests.get(self.url).text
            soup = BeautifulSoup(page, 'html.parser')
            # Adapted from: https://stackoverflow.com/a/34718858
            return [self.url + node.get('href') for node in soup.find_all('a')
                    if node.get('href').endswith(self.ext)]
        except Exception as e:
            print(e)
            return ['Something went wrong! Please check the input.']


if __name__ == '__main__':
    url_args = argparse.ArgumentParser(description='Extract urls from webpage')
    url_args.add_argument('--url', help='Index of/ page URL', required=True,
                          type=str)
    url_args.add_argument('--ext', help='Extension of the file URL to extract',
                          required=True, type=str)

    args = url_args.parse_args()
    url = args.url
    ext = args.ext

    index_of = GetFileLinks(url, ext)
    index_of.get_file_links()
