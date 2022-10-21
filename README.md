# This repository contains a small part of the practical tasks that I did during the training, and I will add and update them over time.

## Tasks

- [paginathion.py](https://github.com/tendil/Tasks-are-different/blob/main/paginathion.py)
<details>
<summary> 
Description of this job
</summary>
<br>
Here I created a Pagination class that processes some content page by page. Pagination is used to divide long lists into pages.
The constructor takes two parameters:

items (default: []): - a list of string content that we will paginate

page_size (default: 10): number of row instances to show per page

The class implements the get_visible_items function that returns the items on the current page.

The class must also provide a set of functions for navigating through pages:

prev_page # go to the previous page

next_page # go to the next page

first_page # jump to the first page

last_page # go to the last page

go_to_page # takes a page number as an argument, navigates to a specific page
            # if passed number > number of pages, then go to the last, if < 1 then go to the first


Also, the class supports the following functions:

get_current_page returns the current page number

get_page_size returns the page size

get_items returns a list of strings

For example, we can create our class like this:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
 
p = Pagination(alphabetList, 4)
And then call get_visible_items to display the contents of the current page (the current page is the first one)

p.get_visible_items() ➞ ["a", "b", "c", "d"]
If we go to the next page and call get_visible_items again, we get ["e", "f", "g", "h"]

p.next_page()
 
p.get_visible_items() ➞ ["e", "f", "g", "h"]
The last page should only have two items, so if we call last_page and get_visible_items we get ["y", "z"]

p.last_page()
p.get_visible_items() ➞ ["y", "z"]
notes

The page_size argument and the go_to_page function argument are only passed as int type, no need to defend against float.

The paging functions must be implemented in such a way that they can be called in chain: p.next_page().next_page().prev_page()
p.last_page().prev_page()
p.first_page().next_page()
p.go_to_page(10).next_page()
</details>

---

- [base_class.py](https://github.com/tendil/Tasks-are-different/blob/main/base_class.py)
> In this file, I have implemented the hierarchy of employees at work into Python classes and objects, where employees can interact with each other.

---

- [Все решения задачек с беспл курса.py](https://github.com/tendil/Tasks-are-different/blob/main/%D0%92%D1%81%D0%B5%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B5%D0%BA%20%D1%81%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%20%D0%BA%D1%83%D1%80%D1%81%D0%B0.py)
> In this file, I just wrote down solutions for small problems for myself.

---

- [ДЗ-10: Ханойские башни.py](https://github.com/tendil/Tasks-are-different/blob/main/%D0%94%D0%97-10:%20%D0%A5%D0%B0%D0%BD%D0%BE%D0%B9%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B1%D0%B0%D1%88%D0%BD%D0%B8.py)
> Tower of Hanoi logic game.
> Here is programmed the very formula for counting the number of steps to complete the game.
>
> The solve_hanoi_tower function was written, which takes the number of disks and returns the minimum number of moves for which the problem can be > solved.

---

- [ДЗ: Кто выстрелил быстрее?.py](https://github.com/tendil/Tasks-are-different/blob/main/%D0%94%D0%97:%20%D0%9A%D1%82%D0%BE%20%D0%B2%D1%8B%D1%81%D1%82%D1%80%D0%B5%D0%BB%D0%B8%D0%BB%20%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%B5%D0%B5%3F.py)
> This implements the whos_first function, which takes two strings and returns the name of the player who fired first.
>
> If the players fired at the same time, then the string "tie" is returned.

---

- [рекурсия.py](https://github.com/tendil/Tasks-are-different/blob/main/%D1%80%D0%B5%D0%BA%D1%83%D1%80%D1%81%D0%B8%D1%8F.py)
> In this file, I analyzed the recursion in which the sequence of chillel is given, and the task is to find the sum of numbers from this sequence.

---

- [сердечко.py](https://github.com/tendil/Tasks-are-different/blob/main/%D1%81%D0%B5%D1%80%D0%B4%D0%B5%D1%87%D0%BA%D0%BE.py)
> Here I've implemented a function that does gradual drawing of a heart using the turtle library.
> See gif below



---

## License

[MIT License](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F_MIT)

## Support

### For support, telegram [@XllrepoDewelloper](https://t.me/XllrepoDewelloper)

## Feedback

### If you have any feedback, telegram [@XllrepoDewelloper](https://t.me/XllrepoDewelloper)

## Contributing

### Contributions are always welcome!

