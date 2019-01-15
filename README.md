プログラムの内容 / 工夫したところ / 苦労
した点 / やりたりなかったこと/コメント




プログラムの内容は日本のいくつかの都市の内三つの都市の気温を表示、また三つの都市の平均との気温差を表示してグラフに表示した。たとえば気温が近い三つの都市を比べる場合気温の絶対値のグラフではどこが比較的暖かくどこが比較的寒いのかわかりにくい。そこがわかりやすくなるために三つの都市の平均とそれぞれとの差を示した二つ目のグラフを用意した。

工夫したところは最後に付け加えた最後に付け加えた『下のグラフの縦軸の大きさを変えよう』のところだ。三つの都市の選び方によって平均との気温差が十五度以上ある組み合わせや、三度ほどの気温差しかない場合もある。そこを手動でグラフを変えることで気温差の大小を視覚的に対話的な行動によってわかるようにした。自動でグラフを書かせて綺麗に枠内にする方法も考えたが平均であるゼロがグラフの真ん中に来ることは不可欠なのでこのようにした。　いま考え直すと選択式でもよかったかもしれないがぽちぽちボタンを連打するのも面白いと思うので変えないことにした。　この自分でグラフのy軸を定めるプログラムはずっとうまくいかずわけがわかりませんでした。ほかの箇所とおなじようにJavaScriptをかいているのになんでGET aval=15と表示されないのだろうとずっと悪戦苦闘していました。　そしたらindex.htmlでavalの入力の上限と下限を決めたら作動するようになり驚きました。

もう一つ工夫したことは一つ目の気温のグラフの縦軸の気温を固定したことだ。元々は縦軸の気温の最小最大は定めていなかったのでそれぞれの指定した年によって自動的にグラフの縦軸が変化していた。しかしそれだと気温の比較が視覚的にしにくいと思い　　　plt.ylim(ymax=32)  plt.ylim(ymin=-8)　とy軸の最大最小を固定しておいた。

苦労した点はやはりデバグがうまく表示されないことだった。きちんとjsでは設定したはずなのに設定が反映されていないことはなんどもあった。先生が言ったようにGoogle Chromeの場合 はデベロパーツールを開いた状態で、リロードボタンを長押しすることでChromeできちんと作動するようになったが,何度か何故かリロードしない時もあった。しかし何故か1日たつときちんと読み込まれるようになっていたりした日もあった。コードを書くこと以外にデベロッパーツールできちんとうまく作動できているのか確認しないといけないということによって大幅に時間がかかった。


プログラミングはコードを書くだけじゃないとはよく聞いていて、それは知らないことをたくさん調べる必要があるからだと思っていたが、わからないことを調べるだけじゃなく書いたコードが正しく動くかテストすることにもたくさん時間がかかるのだと知った。


やり足りなかった点は、毎年のある月のデータのみを使ってグラフを書く機能を付け加えたかった。例えば毎年の6月のみを使って1945年から2018年にかけて本当に地球温暖化が起こっているのか視覚的に確かめたかった。　１２個ある月のうち特定の月のみを取り出す方法がわからなかったのでやった。今のままあと1月から12月までのすべてのデータがあり50年分の情報を見ても一年ごとの周期的な変化が大きかったために年ごとの変化を見ることができなかった。今回作ったプログラムを友達に見せた時必ず地球温暖化は実際に起きているのか聞かれたので同じ月だけ比べられるようにしたかった。


この課題のグラフからわかること
このグラフからは日本の各都市を比べると夏の気温差は大差ないが（札幌と那覇で５℃程度の差）、冬の気温差はとても大きいということがわかる（札幌と那覇で２０℃程度の差）

先生の授業は色々なwebプログラミングについて実際に手を動かすことで浅く広く学ぶことができました。pythonやJavaScript の使い方は既習者にとってはとっても基本的なことでも自分で調べて学ぶとなるととっても難しいということがわかりました。一見基本的なことを先生が直接たくさんの説明で教えてくれるのではなく、少ない説明で実際にやって見ることで知識ではなくwebプログラミングにおいて必要な自分でやって見る力調べる力が身についたように思えます。



