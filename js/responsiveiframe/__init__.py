from fanstatic import Library, Resource
import js.jquery

library = Library('responsiveiframe', 'resources')

responsiveiframe = Resource(
    library, 'jquery.responsiveiframe.js',
    depends=[js.jquery.jquery])
