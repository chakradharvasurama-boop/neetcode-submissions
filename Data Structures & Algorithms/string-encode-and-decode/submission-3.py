class Solution:

    def encode(self, strs: List[str]) -> str:

        return ''.join([s+',a,a,' for s in strs])

    def decode(self, s: str) -> List[str]:
   
        l=s.split(',a,a,')
        return l[:-1]
