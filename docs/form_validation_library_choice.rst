The Problem (The Why? of Form Library)
======================================

So why use a form validation and generation library and not just write plain forms customized to one's heart's content in the view templates? Here are some reasons:

* Not all forms need extensive customization, backend admin panels normally need CRUD interfaces
* Front-end forms visible to site visitors normally do need customization so even if we use a form library, it should provide easy customization options in case we need it
* Building lots of forms and doing their validation tends to get boring pretty quickly, so if it can be done effectively and quickly, it is appreciated
* Centralized validation (most of it derived from the model) eliminates code duplication for validation at schema/model level and at form level
* And there may be more reasons but right now I can't think of any

The choices
===========

In the project introduction, I mentioned something along the lines:

* **Automatic form generation from database/SQLAlchemy models** (looking into possible options like sprox, formalchemy, wtforms, deform, etc)

Did some digging and finalized two contenders, **sprox** and **wtforms**

WTForms
-------

WTForms is small easy to use and easy to learn. Has good structure (IMHO) for validation and object population etc. More complex structures can be built on top of that. But it is a lower level library, perhaps similar on the level to the much complex (and much difficult to develop and sometimes use) toscawidgets library.

Problems
+++++++++

* Just basic forms library, no higher auto-generated model-backed CRUD intefaces (which sprox offers).


Sprox
-----

Provides whole CRUD interfaces with just few lines. Uses ToscaWidgets (Not TW2) behind the scenes. Has some Dojo support which we're also aiming at. Basically Sprox is something that fits in nicely for our requirements. But ....... :-(

Problems
++++++++
* Sprox is based on ToscaWidgets and the scene with ToscaWidgets is not quite clear. The ToscaWidgets 2 branch has existed for years now but still Toscawidgets 1 is used more commonly. Toscawidgets (both 1 & 2) while aiming to be very powerful and flexible also suffers from the complexity that comes with such aims.

* Developing custom widgets for toscawidgets isn't all that easy; I have written some dojo charting widgets for TW2. While TW and TW2 tries to handle a lot of things like resource injection etc, this complexity is a deterrant.


Conclusion
==========

Using sprox reduces a lot of time that would be otherwise spent on building another implementation similar to Sprox but which uses WTForms as its backend instead of ToscaWidgets and isn't just coupled with SQLAlchemy as the ORM (at this time).

But I am inclined to choose **WTForms** though this means ending up building another sprox-like implementation. I believe that building upon WTForms won't be that painful and since WTForms does provide better methods to populate objects and read values from object, its forms are less coupled with the backend ORM engine. Though for PyCK we will be using SQLAlchemy, this does allow some reusability that can be contributed back to the WTForms project. Also I seem to have a gut feeling about using WTForms ;-)

**So the decision is to use WTForms and build a Sprox-like library on top of it that provides simple and Dojo based forms and other display widgets (tables, etc).**

