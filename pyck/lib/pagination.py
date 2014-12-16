def get_pages(total_recs, current_page, recs_per_page=10, max_pages=10):
    """
    A utility function that returns the pages (for records pagination display purposes)

    :param total_recs:
        Total number of records
    :param current_page:
        Current page that is being displayed
    :param recs_per_page:
        Number of records being displayed per page
    :param max_pages:
        Maximum number of pages to return

    Returns a list containing pages that should be displayed as page links.
    """

    total_pages = int(total_recs/recs_per_page)

    if total_recs % recs_per_page > 0:
        total_pages += 1

    pages = []
    if 0 == max_pages % 2:
        pages_before = (max_pages/2)-1
    else:
        pages_before = max_pages/2

    pages_after = int(max_pages/2)
    pages_before = int(pages_before)
    start_page = 1

    if total_pages <= max_pages:
        for i in range(1, total_pages+1):
            pages.append(i)
    else:
        pages_left = max_pages - 1
        if current_page - pages_before <= 0:
            pages_before = current_page - 1

        if current_page + pages_after > total_pages:
            pages_before += ((current_page + pages_after) - total_pages)

        start_page = current_page - pages_before
        for i in range(start_page, current_page + 1):
            pages.append(i)
            pages_left -= 1
            start_page += 1

        for i in range(pages_left+1):
            pages.append(start_page)
            start_page += 1

    return pages
