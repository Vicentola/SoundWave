import unittest
import os
from models import Song, Playlist
from persistence import PersistenceManager
from structures import LinkedList, Stack, Hashtable, BinarySearchTree
from library import MusicLibrary


class Testsong(unittest.TestCase):


    def test_creation(self):
        s = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354.0, genre="Rock")
        self.assertEqual(s.title, "Bohemian Rhapsody")
        self.assertEqual(s.artist, "Queen")
        self.assertEqual(s.play_count, 0)
        
    def test_mark_as_played(self):
        s = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354.0, genre="Rock")
        s.mark_as_played()
        self.assertEqual(s.play_count, 1)
        s.mark_as_played()
        self.assertEqual(s.play_count, 2)
        
    def test_duration_str(self):
        s = Song("X", "Y", "Z", 354.0)
        self.assertEqual(s.duration_str, "05:54")
        
        
    
class TestLinkedList(unittest.TestCase):
    
    
    def test_append(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "LinkedList(10, 20, 30)")
    
    
    def test_pop_front(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(ll.pop_front(), 10)
        self.assertEqual(ll.size, 2)
        self.assertEqual(str(ll), "LinkedList(20, 30)")
        
        
    def test_pop_front_empty(self):
        ll = LinkedList()
        with self.assertRaises(IndexError):
            ll.pop_front()
            
        
    
    
class TestStack(unittest.TestCase):
    
    def test_push_and_peek(self):
        st = Stack(max_size=3)
        st.push("Bohemian Rhapsody")
        st.push("Hotel California")
        st.push("Billie Jean")
        self.assertEqual(st.peek(), "Billie Jean")
        st.push("Superstition")  # deve descartar o mais antigo
        self.assertEqual(st.peek(), "Superstition")
        self.assertEqual(len(st), 3)
        
    def test_pop(self):
        st = Stack(max_size=3)
        st.push("Bohemian Rhapsody")
        st.push("Hotel California")
        st.push("Billie Jean")
        self.assertEqual(st.pop(), "Billie Jean")
        self.assertEqual(st.peek(), "Hotel California")
        self.assertEqual(len(st), 2)
        
    def test_max_size(self):
        st = Stack(max_size=2)
        st.push("Bohemian Rhapsody")
        st.push("Hotel California")
        st.push("Billie Jean")  # deve descartar "Bohemian Rhapsody"
        self.assertEqual(st.peek(), "Billie Jean")
        self.assertEqual(len(st), 2)
        
    def test_pop_empty(self):
        st = Stack(max_size=3)
        with self.assertRaises(IndexError):
            st.pop()
            
            
            
class TestMusicLibrary(unittest.TestCase):
    
    def test_add_and_search(self):
        lib = MusicLibrary()
        s1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354.0, genre="Rock")
        s2 = Song("Creep", "Radiohead", "Pablo Honey", 238.0, genre="Rock")
        s3 = Song("Billie Jean", "Michael Jackson", "Thriller", 294.0, genre="Pop")
        lib.add_song(s1)
        lib.add_song(s2)
        lib.add_song(s3)
        
        self.assertEqual(lib.get_songs_by_artist("Queen"), [s1])
        self.assertEqual(lib.get_songs_by_genre("Rock"), [s1, s2])
        self.assertEqual(lib.search("billie"), [s3])
        
    def test_get_songs_by_genre(self):
        lib = MusicLibrary()
        s1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354.0, genre="Rock")
        s2 = Song("Creep", "Radiohead", "Pablo Honey", 238.0, genre="Rock")
        s3 = Song("Billie Jean", "Michael Jackson", "Thriller", 294.0, genre="Pop")
        lib.add_song(s1)
        lib.add_song(s2)
        lib.add_song(s3)
        
        self.assertEqual(lib.get_songs_by_genre("Rock"), [s1, s2])
        self.assertEqual(lib.get_songs_by_genre("Pop"), [s3])
        self.assertEqual(lib.get_songs_by_genre("Jazz"), [])
        
        
        
        
class TestPersistenceManager(unittest.TestCase):
    
    def test_save_and_load(self):
        lib = MusicLibrary()
        s1 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354.0, genre="Rock")
        s2 = Song("Creep", "Radiohead", "Pablo Honey", 238.0, genre="Rock")
        s3 = Song("Billie Jean", "Michael Jackson", "Thriller", 294.0, genre="Pop")
        lib.add_song(s1)
        lib.add_song(s2)
        lib.add_song(s3)

        pm = PersistenceManager("test_data.json")
        pm.save(lib)

        lib2 = MusicLibrary()
        pm.load(lib2)

        self.assertEqual(len(lib2._songs), 3)
        self.assertEqual(lib2._songs["Bohemian Rhapsody"].artist, "Queen")
        self.assertEqual(lib2._songs["Creep"].artist, "Radiohead")
        self.assertEqual(lib2._songs["Billie Jean"].artist, "Michael Jackson")
        os.remove("test_data.json")
 
    def test_load_empty_file(self):
        pm = PersistenceManager("non_existent_file.json")
        lib = MusicLibrary()
        pm.load(lib)
        self.assertEqual(len(lib._songs), 0)
            
if __name__ == "__main__":
    unittest.main()
        
    
        
        