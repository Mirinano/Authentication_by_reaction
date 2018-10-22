# Authentication_by_reaction

このBOTは、リアクション操作による自動認証システムを実現するためのBOTです。

BOTには次の権限を与える必要があります。

1. メッセージを管理

2. キック

また、BOTを動かすにあたっての注意点は次の通りです。

1. 該当チャンネルで、すべてのユーザーから「リアクションを追加」権限を不許可にすること。

2. このBOT単体では、同意、不同意のアナウンスや、リアクションを用意したりすることができないこと。

3. BOTが閲覧できるチャンネルを同意、不同意の確認を行うチャンネルだけに制限すること

4. 3が難しい場合、max_messagesの枠から該当メッセージが追い出されてしまった場合に反応できなくなるので、できるだけ高頻度で再起動をするようにすること。