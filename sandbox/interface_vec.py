from vec import *
from decl import *

cls = class_(vec2)
cls.slot('x', float)
cls.slot('y', float)
cls.method('__init__', float, float)
cls.method('__repr__')
cls.method('dot', vec2)
cls.method('length')
cls.method('normalize')
cls.method('__pos__')
cls.method('__neg__')
cls.method('__abs__')
cls.method('__add__', (vec2, float))
cls.method('__radd__', float)
cls.method('__sub__', (vec2, float))
cls.method('__rsub__', float)
cls.method('__mul__', (vec2, float))
cls.method('__rmul__', float)
cls.method('__div__', (vec2, float))
cls.method('__rdiv__', float)
cls.getter('r')
cls.getter('xx')
cls.getter('rr')
cls.getter('xxx')
cls.getter('rrr')
cls.getter('xxxx')
cls.getter('rrrr')
cls.getter('xxxy')
cls.getter('rrrg')
cls.getter('xxy')
cls.getter('rrg')
cls.getter('xxyx')
cls.getter('rrgr')
cls.getter('xxyy')
cls.getter('rrgg')
cls.getter('xy')
cls.getter('rg')
cls.getter('xyx')
cls.getter('rgr')
cls.getter('xyxx')
cls.getter('rgrr')
cls.getter('xyxy')
cls.getter('rgrg')
cls.getter('xyy')
cls.getter('rgg')
cls.getter('xyyx')
cls.getter('rggr')
cls.getter('xyyy')
cls.getter('rggg')
cls.getter('g')
cls.getter('yx')
cls.getter('gr')
cls.getter('yxx')
cls.getter('grr')
cls.getter('yxxx')
cls.getter('grrr')
cls.getter('yxxy')
cls.getter('grrg')
cls.getter('yxy')
cls.getter('grg')
cls.getter('yxyx')
cls.getter('grgr')
cls.getter('yxyy')
cls.getter('grgg')
cls.getter('yy')
cls.getter('gg')
cls.getter('yyx')
cls.getter('ggr')
cls.getter('yyxx')
cls.getter('ggrr')
cls.getter('yyxy')
cls.getter('ggrg')
cls.getter('yyy')
cls.getter('ggg')
cls.getter('yyyx')
cls.getter('gggr')
cls.getter('yyyy')
cls.getter('gggg')

cls = class_(vec3)
cls.slot('x', float)
cls.slot('y', float)
cls.slot('z', float)
cls.method('__init__', float, float, float)
cls.method('__repr__')
cls.method('dot', vec3)
cls.method('length')
cls.method('normalize')
cls.method('cross', vec3)
cls.method('__pos__')
cls.method('__neg__')
cls.method('__abs__')
cls.method('__add__', (vec3, float))
cls.method('__radd__', float)
cls.method('__sub__', (vec3, float))
cls.method('__rsub__', float)
cls.method('__mul__', (vec3, float))
cls.method('__rmul__', float)
cls.method('__div__', (vec3, float))
cls.method('__rdiv__', float)
cls.getter('r')
cls.getter('xx')
cls.getter('rr')
cls.getter('xxx')
cls.getter('rrr')
cls.getter('xxxx')
cls.getter('rrrr')
cls.getter('xxxy')
cls.getter('rrrg')
cls.getter('xxxz')
cls.getter('rrrb')
cls.getter('xxy')
cls.getter('rrg')
cls.getter('xxyx')
cls.getter('rrgr')
cls.getter('xxyy')
cls.getter('rrgg')
cls.getter('xxyz')
cls.getter('rrgb')
cls.getter('xxz')
cls.getter('rrb')
cls.getter('xxzx')
cls.getter('rrbr')
cls.getter('xxzy')
cls.getter('rrbg')
cls.getter('xxzz')
cls.getter('rrbb')
cls.getter('xy')
cls.getter('rg')
cls.getter('xyx')
cls.getter('rgr')
cls.getter('xyxx')
cls.getter('rgrr')
cls.getter('xyxy')
cls.getter('rgrg')
cls.getter('xyxz')
cls.getter('rgrb')
cls.getter('xyy')
cls.getter('rgg')
cls.getter('xyyx')
cls.getter('rggr')
cls.getter('xyyy')
cls.getter('rggg')
cls.getter('xyyz')
cls.getter('rggb')
cls.getter('xyz')
cls.getter('rgb')
cls.getter('xyzx')
cls.getter('rgbr')
cls.getter('xyzy')
cls.getter('rgbg')
cls.getter('xyzz')
cls.getter('rgbb')
cls.getter('xz')
cls.getter('rb')
cls.getter('xzx')
cls.getter('rbr')
cls.getter('xzxx')
cls.getter('rbrr')
cls.getter('xzxy')
cls.getter('rbrg')
cls.getter('xzxz')
cls.getter('rbrb')
cls.getter('xzy')
cls.getter('rbg')
cls.getter('xzyx')
cls.getter('rbgr')
cls.getter('xzyy')
cls.getter('rbgg')
cls.getter('xzyz')
cls.getter('rbgb')
cls.getter('xzz')
cls.getter('rbb')
cls.getter('xzzx')
cls.getter('rbbr')
cls.getter('xzzy')
cls.getter('rbbg')
cls.getter('xzzz')
cls.getter('rbbb')
cls.getter('g')
cls.getter('yx')
cls.getter('gr')
cls.getter('yxx')
cls.getter('grr')
cls.getter('yxxx')
cls.getter('grrr')
cls.getter('yxxy')
cls.getter('grrg')
cls.getter('yxxz')
cls.getter('grrb')
cls.getter('yxy')
cls.getter('grg')
cls.getter('yxyx')
cls.getter('grgr')
cls.getter('yxyy')
cls.getter('grgg')
cls.getter('yxyz')
cls.getter('grgb')
cls.getter('yxz')
cls.getter('grb')
cls.getter('yxzx')
cls.getter('grbr')
cls.getter('yxzy')
cls.getter('grbg')
cls.getter('yxzz')
cls.getter('grbb')
cls.getter('yy')
cls.getter('gg')
cls.getter('yyx')
cls.getter('ggr')
cls.getter('yyxx')
cls.getter('ggrr')
cls.getter('yyxy')
cls.getter('ggrg')
cls.getter('yyxz')
cls.getter('ggrb')
cls.getter('yyy')
cls.getter('ggg')
cls.getter('yyyx')
cls.getter('gggr')
cls.getter('yyyy')
cls.getter('gggg')
cls.getter('yyyz')
cls.getter('gggb')
cls.getter('yyz')
cls.getter('ggb')
cls.getter('yyzx')
cls.getter('ggbr')
cls.getter('yyzy')
cls.getter('ggbg')
cls.getter('yyzz')
cls.getter('ggbb')
cls.getter('yz')
cls.getter('gb')
cls.getter('yzx')
cls.getter('gbr')
cls.getter('yzxx')
cls.getter('gbrr')
cls.getter('yzxy')
cls.getter('gbrg')
cls.getter('yzxz')
cls.getter('gbrb')
cls.getter('yzy')
cls.getter('gbg')
cls.getter('yzyx')
cls.getter('gbgr')
cls.getter('yzyy')
cls.getter('gbgg')
cls.getter('yzyz')
cls.getter('gbgb')
cls.getter('yzz')
cls.getter('gbb')
cls.getter('yzzx')
cls.getter('gbbr')
cls.getter('yzzy')
cls.getter('gbbg')
cls.getter('yzzz')
cls.getter('gbbb')
cls.getter('b')
cls.getter('zx')
cls.getter('br')
cls.getter('zxx')
cls.getter('brr')
cls.getter('zxxx')
cls.getter('brrr')
cls.getter('zxxy')
cls.getter('brrg')
cls.getter('zxxz')
cls.getter('brrb')
cls.getter('zxy')
cls.getter('brg')
cls.getter('zxyx')
cls.getter('brgr')
cls.getter('zxyy')
cls.getter('brgg')
cls.getter('zxyz')
cls.getter('brgb')
cls.getter('zxz')
cls.getter('brb')
cls.getter('zxzx')
cls.getter('brbr')
cls.getter('zxzy')
cls.getter('brbg')
cls.getter('zxzz')
cls.getter('brbb')
cls.getter('zy')
cls.getter('bg')
cls.getter('zyx')
cls.getter('bgr')
cls.getter('zyxx')
cls.getter('bgrr')
cls.getter('zyxy')
cls.getter('bgrg')
cls.getter('zyxz')
cls.getter('bgrb')
cls.getter('zyy')
cls.getter('bgg')
cls.getter('zyyx')
cls.getter('bggr')
cls.getter('zyyy')
cls.getter('bggg')
cls.getter('zyyz')
cls.getter('bggb')
cls.getter('zyz')
cls.getter('bgb')
cls.getter('zyzx')
cls.getter('bgbr')
cls.getter('zyzy')
cls.getter('bgbg')
cls.getter('zyzz')
cls.getter('bgbb')
cls.getter('zz')
cls.getter('bb')
cls.getter('zzx')
cls.getter('bbr')
cls.getter('zzxx')
cls.getter('bbrr')
cls.getter('zzxy')
cls.getter('bbrg')
cls.getter('zzxz')
cls.getter('bbrb')
cls.getter('zzy')
cls.getter('bbg')
cls.getter('zzyx')
cls.getter('bbgr')
cls.getter('zzyy')
cls.getter('bbgg')
cls.getter('zzyz')
cls.getter('bbgb')
cls.getter('zzz')
cls.getter('bbb')
cls.getter('zzzx')
cls.getter('bbbr')
cls.getter('zzzy')
cls.getter('bbbg')
cls.getter('zzzz')
cls.getter('bbbb')

cls = class_(vec4)
cls.slot('x', float)
cls.slot('y', float)
cls.slot('z', float)
cls.slot('w', float)
cls.method('__init__', float, float, float, float)
cls.method('__repr__')
cls.method('dot', vec4)
cls.method('length')
cls.method('normalize')
cls.method('__pos__')
cls.method('__neg__')
cls.method('__abs__')
cls.method('__add__', (vec4, float))
cls.method('__radd__', float)
cls.method('__sub__', (vec4, float))
cls.method('__rsub__', float)
cls.method('__mul__', (vec4, float))
cls.method('__rmul__', float)
cls.method('__div__', (vec4, float))
cls.method('__rdiv__', float)
cls.getter('r')
cls.getter('xx')
cls.getter('rr')
cls.getter('xxx')
cls.getter('rrr')
cls.getter('xxxx')
cls.getter('rrrr')
cls.getter('xxxy')
cls.getter('rrrg')
cls.getter('xxxz')
cls.getter('rrrb')
cls.getter('xxxw')
cls.getter('rrra')
cls.getter('xxy')
cls.getter('rrg')
cls.getter('xxyx')
cls.getter('rrgr')
cls.getter('xxyy')
cls.getter('rrgg')
cls.getter('xxyz')
cls.getter('rrgb')
cls.getter('xxyw')
cls.getter('rrga')
cls.getter('xxz')
cls.getter('rrb')
cls.getter('xxzx')
cls.getter('rrbr')
cls.getter('xxzy')
cls.getter('rrbg')
cls.getter('xxzz')
cls.getter('rrbb')
cls.getter('xxzw')
cls.getter('rrba')
cls.getter('xxw')
cls.getter('rra')
cls.getter('xxwx')
cls.getter('rrar')
cls.getter('xxwy')
cls.getter('rrag')
cls.getter('xxwz')
cls.getter('rrab')
cls.getter('xxww')
cls.getter('rraa')
cls.getter('xy')
cls.getter('rg')
cls.getter('xyx')
cls.getter('rgr')
cls.getter('xyxx')
cls.getter('rgrr')
cls.getter('xyxy')
cls.getter('rgrg')
cls.getter('xyxz')
cls.getter('rgrb')
cls.getter('xyxw')
cls.getter('rgra')
cls.getter('xyy')
cls.getter('rgg')
cls.getter('xyyx')
cls.getter('rggr')
cls.getter('xyyy')
cls.getter('rggg')
cls.getter('xyyz')
cls.getter('rggb')
cls.getter('xyyw')
cls.getter('rgga')
cls.getter('xyz')
cls.getter('rgb')
cls.getter('xyzx')
cls.getter('rgbr')
cls.getter('xyzy')
cls.getter('rgbg')
cls.getter('xyzz')
cls.getter('rgbb')
cls.getter('xyzw')
cls.getter('rgba')
cls.getter('xyw')
cls.getter('rga')
cls.getter('xywx')
cls.getter('rgar')
cls.getter('xywy')
cls.getter('rgag')
cls.getter('xywz')
cls.getter('rgab')
cls.getter('xyww')
cls.getter('rgaa')
cls.getter('xz')
cls.getter('rb')
cls.getter('xzx')
cls.getter('rbr')
cls.getter('xzxx')
cls.getter('rbrr')
cls.getter('xzxy')
cls.getter('rbrg')
cls.getter('xzxz')
cls.getter('rbrb')
cls.getter('xzxw')
cls.getter('rbra')
cls.getter('xzy')
cls.getter('rbg')
cls.getter('xzyx')
cls.getter('rbgr')
cls.getter('xzyy')
cls.getter('rbgg')
cls.getter('xzyz')
cls.getter('rbgb')
cls.getter('xzyw')
cls.getter('rbga')
cls.getter('xzz')
cls.getter('rbb')
cls.getter('xzzx')
cls.getter('rbbr')
cls.getter('xzzy')
cls.getter('rbbg')
cls.getter('xzzz')
cls.getter('rbbb')
cls.getter('xzzw')
cls.getter('rbba')
cls.getter('xzw')
cls.getter('rba')
cls.getter('xzwx')
cls.getter('rbar')
cls.getter('xzwy')
cls.getter('rbag')
cls.getter('xzwz')
cls.getter('rbab')
cls.getter('xzww')
cls.getter('rbaa')
cls.getter('xw')
cls.getter('ra')
cls.getter('xwx')
cls.getter('rar')
cls.getter('xwxx')
cls.getter('rarr')
cls.getter('xwxy')
cls.getter('rarg')
cls.getter('xwxz')
cls.getter('rarb')
cls.getter('xwxw')
cls.getter('rara')
cls.getter('xwy')
cls.getter('rag')
cls.getter('xwyx')
cls.getter('ragr')
cls.getter('xwyy')
cls.getter('ragg')
cls.getter('xwyz')
cls.getter('ragb')
cls.getter('xwyw')
cls.getter('raga')
cls.getter('xwz')
cls.getter('rab')
cls.getter('xwzx')
cls.getter('rabr')
cls.getter('xwzy')
cls.getter('rabg')
cls.getter('xwzz')
cls.getter('rabb')
cls.getter('xwzw')
cls.getter('raba')
cls.getter('xww')
cls.getter('raa')
cls.getter('xwwx')
cls.getter('raar')
cls.getter('xwwy')
cls.getter('raag')
cls.getter('xwwz')
cls.getter('raab')
cls.getter('xwww')
cls.getter('raaa')
cls.getter('g')
cls.getter('yx')
cls.getter('gr')
cls.getter('yxx')
cls.getter('grr')
cls.getter('yxxx')
cls.getter('grrr')
cls.getter('yxxy')
cls.getter('grrg')
cls.getter('yxxz')
cls.getter('grrb')
cls.getter('yxxw')
cls.getter('grra')
cls.getter('yxy')
cls.getter('grg')
cls.getter('yxyx')
cls.getter('grgr')
cls.getter('yxyy')
cls.getter('grgg')
cls.getter('yxyz')
cls.getter('grgb')
cls.getter('yxyw')
cls.getter('grga')
cls.getter('yxz')
cls.getter('grb')
cls.getter('yxzx')
cls.getter('grbr')
cls.getter('yxzy')
cls.getter('grbg')
cls.getter('yxzz')
cls.getter('grbb')
cls.getter('yxzw')
cls.getter('grba')
cls.getter('yxw')
cls.getter('gra')
cls.getter('yxwx')
cls.getter('grar')
cls.getter('yxwy')
cls.getter('grag')
cls.getter('yxwz')
cls.getter('grab')
cls.getter('yxww')
cls.getter('graa')
cls.getter('yy')
cls.getter('gg')
cls.getter('yyx')
cls.getter('ggr')
cls.getter('yyxx')
cls.getter('ggrr')
cls.getter('yyxy')
cls.getter('ggrg')
cls.getter('yyxz')
cls.getter('ggrb')
cls.getter('yyxw')
cls.getter('ggra')
cls.getter('yyy')
cls.getter('ggg')
cls.getter('yyyx')
cls.getter('gggr')
cls.getter('yyyy')
cls.getter('gggg')
cls.getter('yyyz')
cls.getter('gggb')
cls.getter('yyyw')
cls.getter('ggga')
cls.getter('yyz')
cls.getter('ggb')
cls.getter('yyzx')
cls.getter('ggbr')
cls.getter('yyzy')
cls.getter('ggbg')
cls.getter('yyzz')
cls.getter('ggbb')
cls.getter('yyzw')
cls.getter('ggba')
cls.getter('yyw')
cls.getter('gga')
cls.getter('yywx')
cls.getter('ggar')
cls.getter('yywy')
cls.getter('ggag')
cls.getter('yywz')
cls.getter('ggab')
cls.getter('yyww')
cls.getter('ggaa')
cls.getter('yz')
cls.getter('gb')
cls.getter('yzx')
cls.getter('gbr')
cls.getter('yzxx')
cls.getter('gbrr')
cls.getter('yzxy')
cls.getter('gbrg')
cls.getter('yzxz')
cls.getter('gbrb')
cls.getter('yzxw')
cls.getter('gbra')
cls.getter('yzy')
cls.getter('gbg')
cls.getter('yzyx')
cls.getter('gbgr')
cls.getter('yzyy')
cls.getter('gbgg')
cls.getter('yzyz')
cls.getter('gbgb')
cls.getter('yzyw')
cls.getter('gbga')
cls.getter('yzz')
cls.getter('gbb')
cls.getter('yzzx')
cls.getter('gbbr')
cls.getter('yzzy')
cls.getter('gbbg')
cls.getter('yzzz')
cls.getter('gbbb')
cls.getter('yzzw')
cls.getter('gbba')
cls.getter('yzw')
cls.getter('gba')
cls.getter('yzwx')
cls.getter('gbar')
cls.getter('yzwy')
cls.getter('gbag')
cls.getter('yzwz')
cls.getter('gbab')
cls.getter('yzww')
cls.getter('gbaa')
cls.getter('yw')
cls.getter('ga')
cls.getter('ywx')
cls.getter('gar')
cls.getter('ywxx')
cls.getter('garr')
cls.getter('ywxy')
cls.getter('garg')
cls.getter('ywxz')
cls.getter('garb')
cls.getter('ywxw')
cls.getter('gara')
cls.getter('ywy')
cls.getter('gag')
cls.getter('ywyx')
cls.getter('gagr')
cls.getter('ywyy')
cls.getter('gagg')
cls.getter('ywyz')
cls.getter('gagb')
cls.getter('ywyw')
cls.getter('gaga')
cls.getter('ywz')
cls.getter('gab')
cls.getter('ywzx')
cls.getter('gabr')
cls.getter('ywzy')
cls.getter('gabg')
cls.getter('ywzz')
cls.getter('gabb')
cls.getter('ywzw')
cls.getter('gaba')
cls.getter('yww')
cls.getter('gaa')
cls.getter('ywwx')
cls.getter('gaar')
cls.getter('ywwy')
cls.getter('gaag')
cls.getter('ywwz')
cls.getter('gaab')
cls.getter('ywww')
cls.getter('gaaa')
cls.getter('b')
cls.getter('zx')
cls.getter('br')
cls.getter('zxx')
cls.getter('brr')
cls.getter('zxxx')
cls.getter('brrr')
cls.getter('zxxy')
cls.getter('brrg')
cls.getter('zxxz')
cls.getter('brrb')
cls.getter('zxxw')
cls.getter('brra')
cls.getter('zxy')
cls.getter('brg')
cls.getter('zxyx')
cls.getter('brgr')
cls.getter('zxyy')
cls.getter('brgg')
cls.getter('zxyz')
cls.getter('brgb')
cls.getter('zxyw')
cls.getter('brga')
cls.getter('zxz')
cls.getter('brb')
cls.getter('zxzx')
cls.getter('brbr')
cls.getter('zxzy')
cls.getter('brbg')
cls.getter('zxzz')
cls.getter('brbb')
cls.getter('zxzw')
cls.getter('brba')
cls.getter('zxw')
cls.getter('bra')
cls.getter('zxwx')
cls.getter('brar')
cls.getter('zxwy')
cls.getter('brag')
cls.getter('zxwz')
cls.getter('brab')
cls.getter('zxww')
cls.getter('braa')
cls.getter('zy')
cls.getter('bg')
cls.getter('zyx')
cls.getter('bgr')
cls.getter('zyxx')
cls.getter('bgrr')
cls.getter('zyxy')
cls.getter('bgrg')
cls.getter('zyxz')
cls.getter('bgrb')
cls.getter('zyxw')
cls.getter('bgra')
cls.getter('zyy')
cls.getter('bgg')
cls.getter('zyyx')
cls.getter('bggr')
cls.getter('zyyy')
cls.getter('bggg')
cls.getter('zyyz')
cls.getter('bggb')
cls.getter('zyyw')
cls.getter('bgga')
cls.getter('zyz')
cls.getter('bgb')
cls.getter('zyzx')
cls.getter('bgbr')
cls.getter('zyzy')
cls.getter('bgbg')
cls.getter('zyzz')
cls.getter('bgbb')
cls.getter('zyzw')
cls.getter('bgba')
cls.getter('zyw')
cls.getter('bga')
cls.getter('zywx')
cls.getter('bgar')
cls.getter('zywy')
cls.getter('bgag')
cls.getter('zywz')
cls.getter('bgab')
cls.getter('zyww')
cls.getter('bgaa')
cls.getter('zz')
cls.getter('bb')
cls.getter('zzx')
cls.getter('bbr')
cls.getter('zzxx')
cls.getter('bbrr')
cls.getter('zzxy')
cls.getter('bbrg')
cls.getter('zzxz')
cls.getter('bbrb')
cls.getter('zzxw')
cls.getter('bbra')
cls.getter('zzy')
cls.getter('bbg')
cls.getter('zzyx')
cls.getter('bbgr')
cls.getter('zzyy')
cls.getter('bbgg')
cls.getter('zzyz')
cls.getter('bbgb')
cls.getter('zzyw')
cls.getter('bbga')
cls.getter('zzz')
cls.getter('bbb')
cls.getter('zzzx')
cls.getter('bbbr')
cls.getter('zzzy')
cls.getter('bbbg')
cls.getter('zzzz')
cls.getter('bbbb')
cls.getter('zzzw')
cls.getter('bbba')
cls.getter('zzw')
cls.getter('bba')
cls.getter('zzwx')
cls.getter('bbar')
cls.getter('zzwy')
cls.getter('bbag')
cls.getter('zzwz')
cls.getter('bbab')
cls.getter('zzww')
cls.getter('bbaa')
cls.getter('zw')
cls.getter('ba')
cls.getter('zwx')
cls.getter('bar')
cls.getter('zwxx')
cls.getter('barr')
cls.getter('zwxy')
cls.getter('barg')
cls.getter('zwxz')
cls.getter('barb')
cls.getter('zwxw')
cls.getter('bara')
cls.getter('zwy')
cls.getter('bag')
cls.getter('zwyx')
cls.getter('bagr')
cls.getter('zwyy')
cls.getter('bagg')
cls.getter('zwyz')
cls.getter('bagb')
cls.getter('zwyw')
cls.getter('baga')
cls.getter('zwz')
cls.getter('bab')
cls.getter('zwzx')
cls.getter('babr')
cls.getter('zwzy')
cls.getter('babg')
cls.getter('zwzz')
cls.getter('babb')
cls.getter('zwzw')
cls.getter('baba')
cls.getter('zww')
cls.getter('baa')
cls.getter('zwwx')
cls.getter('baar')
cls.getter('zwwy')
cls.getter('baag')
cls.getter('zwwz')
cls.getter('baab')
cls.getter('zwww')
cls.getter('baaa')
cls.getter('a')
cls.getter('wx')
cls.getter('ar')
cls.getter('wxx')
cls.getter('arr')
cls.getter('wxxx')
cls.getter('arrr')
cls.getter('wxxy')
cls.getter('arrg')
cls.getter('wxxz')
cls.getter('arrb')
cls.getter('wxxw')
cls.getter('arra')
cls.getter('wxy')
cls.getter('arg')
cls.getter('wxyx')
cls.getter('argr')
cls.getter('wxyy')
cls.getter('argg')
cls.getter('wxyz')
cls.getter('argb')
cls.getter('wxyw')
cls.getter('arga')
cls.getter('wxz')
cls.getter('arb')
cls.getter('wxzx')
cls.getter('arbr')
cls.getter('wxzy')
cls.getter('arbg')
cls.getter('wxzz')
cls.getter('arbb')
cls.getter('wxzw')
cls.getter('arba')
cls.getter('wxw')
cls.getter('ara')
cls.getter('wxwx')
cls.getter('arar')
cls.getter('wxwy')
cls.getter('arag')
cls.getter('wxwz')
cls.getter('arab')
cls.getter('wxww')
cls.getter('araa')
cls.getter('wy')
cls.getter('ag')
cls.getter('wyx')
cls.getter('agr')
cls.getter('wyxx')
cls.getter('agrr')
cls.getter('wyxy')
cls.getter('agrg')
cls.getter('wyxz')
cls.getter('agrb')
cls.getter('wyxw')
cls.getter('agra')
cls.getter('wyy')
cls.getter('agg')
cls.getter('wyyx')
cls.getter('aggr')
cls.getter('wyyy')
cls.getter('aggg')
cls.getter('wyyz')
cls.getter('aggb')
cls.getter('wyyw')
cls.getter('agga')
cls.getter('wyz')
cls.getter('agb')
cls.getter('wyzx')
cls.getter('agbr')
cls.getter('wyzy')
cls.getter('agbg')
cls.getter('wyzz')
cls.getter('agbb')
cls.getter('wyzw')
cls.getter('agba')
cls.getter('wyw')
cls.getter('aga')
cls.getter('wywx')
cls.getter('agar')
cls.getter('wywy')
cls.getter('agag')
cls.getter('wywz')
cls.getter('agab')
cls.getter('wyww')
cls.getter('agaa')
cls.getter('wz')
cls.getter('ab')
cls.getter('wzx')
cls.getter('abr')
cls.getter('wzxx')
cls.getter('abrr')
cls.getter('wzxy')
cls.getter('abrg')
cls.getter('wzxz')
cls.getter('abrb')
cls.getter('wzxw')
cls.getter('abra')
cls.getter('wzy')
cls.getter('abg')
cls.getter('wzyx')
cls.getter('abgr')
cls.getter('wzyy')
cls.getter('abgg')
cls.getter('wzyz')
cls.getter('abgb')
cls.getter('wzyw')
cls.getter('abga')
cls.getter('wzz')
cls.getter('abb')
cls.getter('wzzx')
cls.getter('abbr')
cls.getter('wzzy')
cls.getter('abbg')
cls.getter('wzzz')
cls.getter('abbb')
cls.getter('wzzw')
cls.getter('abba')
cls.getter('wzw')
cls.getter('aba')
cls.getter('wzwx')
cls.getter('abar')
cls.getter('wzwy')
cls.getter('abag')
cls.getter('wzwz')
cls.getter('abab')
cls.getter('wzww')
cls.getter('abaa')
cls.getter('ww')
cls.getter('aa')
cls.getter('wwx')
cls.getter('aar')
cls.getter('wwxx')
cls.getter('aarr')
cls.getter('wwxy')
cls.getter('aarg')
cls.getter('wwxz')
cls.getter('aarb')
cls.getter('wwxw')
cls.getter('aara')
cls.getter('wwy')
cls.getter('aag')
cls.getter('wwyx')
cls.getter('aagr')
cls.getter('wwyy')
cls.getter('aagg')
cls.getter('wwyz')
cls.getter('aagb')
cls.getter('wwyw')
cls.getter('aaga')
cls.getter('wwz')
cls.getter('aab')
cls.getter('wwzx')
cls.getter('aabr')
cls.getter('wwzy')
cls.getter('aabg')
cls.getter('wwzz')
cls.getter('aabb')
cls.getter('wwzw')
cls.getter('aaba')
cls.getter('www')
cls.getter('aaa')
cls.getter('wwwx')
cls.getter('aaar')
cls.getter('wwwy')
cls.getter('aaag')
cls.getter('wwwz')
cls.getter('aaab')
cls.getter('wwww')
cls.getter('aaaa')

cls = class_(mat2)
cls.slot('m00', float)
cls.slot('m01', float)
cls.slot('m10', float)
cls.slot('m11', float)
cls.method('__init__', float, float, float, float)
cls.method('__repr__')
cls.method('__mul__', (vec2, mat2, float))
cls.method('__imul__', (vec2, float))

cls = class_(mat3)
cls.slot('m00', float)
cls.slot('m01', float)
cls.slot('m02', float)
cls.slot('m10', float)
cls.slot('m11', float)
cls.slot('m12', float)
cls.slot('m20', float)
cls.slot('m21', float)
cls.slot('m22', float)
cls.method('__init__', float, float, float, float, float, float, float, float, float)
cls.method('__repr__')
cls.method('__mul__', (vec3, mat3, float))
cls.method('__imul__', (vec3, float))

cls = class_(mat4)
cls.slot('m00', float)
cls.slot('m01', float)
cls.slot('m02', float)
cls.slot('m03', float)
cls.slot('m10', float)
cls.slot('m11', float)
cls.slot('m12', float)
cls.slot('m13', float)
cls.slot('m20', float)
cls.slot('m21', float)
cls.slot('m22', float)
cls.slot('m23', float)
cls.slot('m30', float)
cls.slot('m31', float)
cls.slot('m32', float)
cls.slot('m33', float)
cls.method('__init__', float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float)
cls.method('__repr__')
cls.method('__mul__', (vec4, mat4, float))
cls.method('__imul__', (vec4, float))
