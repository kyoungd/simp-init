from utilGetJwt import GetJwtFromSite
from redisHash import JwtSimpAdmin

if __name__ == '__main__':
    jwt:str = GetJwtFromSite.run()
    app = JwtSimpAdmin()
    app.Add('JWT', {'jwt': jwt})
    print(jwt)
