class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live=timeToLive
        self.token_expiray_date={}
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_expiray_date[tokenId]=currentTime+self.time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_expiray_date and self.token_expiray_date[tokenId]>currentTime:
            self.token_expiray_date[tokenId]=currentTime+self.time_to_live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum([time>currentTime for time in self.token_expiray_date.values()])


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)