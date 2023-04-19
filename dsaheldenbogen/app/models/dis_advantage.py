from __future__ import annotations  # required till PEP 563

from typing import List

from dsaheldenbogen.app.models.base_model import BaseModel


class DisAdvantage(BaseModel):
    """
    Represents either an advantage or a disadvantage.

    Field 'uses' can be empty (meant to be optional)
    TODO make field 'uses' truly optional, handling "None" somewhere
    """
    name: str
    uses: str = ''  # TODO [on TODO list] this should be a function '<feature>("<uses>")'
    level: int = 1

    @staticmethod
    def list_by(dis_advantages: List[tuple]) -> List[DisAdvantage]:
        """
        Convenient method to parse tuples of different length.

        a tuple can have following forms:
         * (name:str, uses:str, level:int)
         * (name:str, uses:str)
         * (name:str, level:int)
         * (name:str,)

        default values:
         * uses := ''
         * level := 1

        for example:
         * ('Unfähig', 'Schwimmen', 2)
         * ('Unfähig', 'Schwimmen')
         * ('Dunkelsicht', 2)
         * ('Dunkelsicht',)
        """
        result = []
        for da in dis_advantages:
            match len(da):
                case 3:
                    # (name:str, uses:str, level:int)
                    result.append(DisAdvantage(name=da[0], uses=da[1], level=da[2]))
                case 2:
                    if type(da[1]) == str:
                        # (name:str, uses:str)
                        result.append(DisAdvantage(name=da[0], uses=da[1]))
                    else:
                        # (name:str, level:int)
                        result.append(DisAdvantage(name=da[0], level=da[1]))
                case 1:
                    # (name:str,)
                    result.append(DisAdvantage(name=da[0]))
        return result
