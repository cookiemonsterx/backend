import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from music.models import Album, Artist, Song

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class SongType(DjangoObjectType):
    class Meta:
        model = Song


class Query(ObjectType):  
    artist = graphene.Field(ArtistType, id=graphene.Int())
    album = graphene.Field(AlbumType, id=graphene.Int())
    song = graphene.Field(SongType, id=graphene.Int())
    artists = graphene.List(ArtistType)
    albums= graphene.List(AlbumType)
    songs = graphene.List(SongType)

    def resolve_artist(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Artist.objects.get(pk=id)

        return None

    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Album.objects.get(pk=id)

        return None

    def resolve_song(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Song.objects.get(pk=id)

        return None
    

    def resolve_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_albums(self, info, **kwargs):
        return Album.objects.all()
    def resolve_songs(self, info, **kwargs):
        return Song.objects.all()




class ArtistInput(graphene.InputObjectType):  
    id = graphene.ID()
    name = graphene.String()

class AlbumInput(graphene.InputObjectType):  
    id = graphene.ID()
    title = graphene.String()
    genre = graphene.String()
    artists = graphene.List(ArtistInput)
    year = graphene.Int()

class SongInput(graphene.InputObjectType):
    title = graphene.String()
    albums = graphene.List(AlbumInput)
    



class CreateArtist(graphene.Mutation):  
    class Arguments:
        input = ArtistInput(required=True)

    ok = graphene.Boolean()
    artist = graphene.Field(ArtistType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        artist_instance = Artist(name=input.name)
        artist_instance.save()
        return CreateArtist(ok=ok, artist=artist_instance)

class UpdateArtist(graphene.Mutation):  
    class Arguments:
        id = graphene.Int(required=True)
        input = ArtistInput(required=True)

    ok = graphene.Boolean()
    artist = graphene.Field(ArtistType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        artist_instance = Artist.objects.get(pk=id)
        if artist_instance:
            ok = True
            artist_instance.name = input.name
            artist_instance.save()
            return UpdateArtist(ok=ok, artist=artist_instance)
        return UpdateArtist(ok=ok, artist=None)





class CreateAlbum(graphene.Mutation):  
    class Arguments:
        input = AlbumInput(required=True)

    ok = graphene.Boolean()
    album = graphene.Field(AlbumType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        artists = []
        for artist_input in input.artist:
          artist = Artist.objects.get(pk=artist_input.id)
          if artist is None:
            return CreateAlbum(ok=False, movie=None)
          artists.append(album)
        album_instance = Album(
          title=input.title,
          genre=input.genre,
          year=input.year
          )
        album_instance.save()
        album_instance.artists.set(artists)
        return CreateAlbum(ok=ok, album=album_instance)


class UpdateAlbum(graphene.Mutation):  
    class Arguments:
        id = graphene.Int(required=True)
        input = AlbumInput(required=True)

    ok = graphene.Boolean()
    album = graphene.Field(AlbumType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        album_instance = Album.objects.get(pk=id)
        if album_instance:
            ok = True
            artists = []
            for artist_input in input.artists:
              artist = Artist.objects.get(pk=artist_input.id)
              if artist is None:
                return UpdateAlbum(ok=False, album=None)
              artists.append(artist)
            album_instance.title=input.title
            album_instance.genre=input.genre
            album_instance.year=input.year.save()
            album_instance.artists.set(artists)
            return UpdateAlbum(ok=ok, album=album_instance)
        return UpdateAlbum(ok=ok, album=None)



class CreateSong(graphene.Mutation):  
    class Arguments:
        input = SongInput(required=True)

    ok = graphene.Boolean()
    song = graphene.Field(SongType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        albums = []
        for albums_input in input.album:
          album = Album.objects.get(pk=artist_input.id)
          if album is None:
            return CreateSong(ok=False, movie=None)
          albums.append(song)
        song_instance = Song(
          title=input.title,
        
          )
        song_instance.save()
        song_instance.albums.set(albums)
        return CreateSong(ok=ok, song=song_instance)


class UpdateSong(graphene.Mutation):  
    class Arguments:
        id = graphene.Int(required=True)
        input = SongInput(required=True)

    ok = graphene.Boolean()
    song = graphene.Field(SongType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        song_instance = Song.objects.get(pk=id)
        if song_instance:
            ok = True
            albums = []
            for album_input in input.albums:
              album = Album.objects.get(pk=album_input.id)
              if album is None:
                return UpdateSong(ok=False, album=None)
              albums.append(album)
            song_instance.title=input.title.save()
            song_instance.albums.set(albums)
            return UpdateSong(ok=ok, song=song_instance)
        return UpdateSong(ok=ok, song=None)

class Mutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()
    update_artist = UpdateArtist.Field()
    create_album = CreateAlbum.Field()
    update_album = CreateAlbum.Field()
    create_song = CreateSong.Field()
    update_song = UpdateSong.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
    

























