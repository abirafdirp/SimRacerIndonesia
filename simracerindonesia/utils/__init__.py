def get_page_range_helper_context(paginator, paginated_object_list):
    # mandatory if you want to include utils/pagination.html
    # this will show a maximum of 7 previous and next pages
    # (15 pages total including the current page)
    # so not all pages link will shown
    index = paginated_object_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 7 if index >= 7 else 0
    end_index = index + 7 if index <= max_index - 7 else max_index

    if start_index != 0:
        show_first_page_link = True
    else:
        show_first_page_link = False

    if end_index != max_index:
        show_last_page_link = True
    else:
        show_last_page_link = False

    return {
        'page_range': paginator.page_range[start_index:end_index],
        'max_index': max_index,
        'show_first_page_link': show_first_page_link,
        'show_last_page_link': show_last_page_link
    }
