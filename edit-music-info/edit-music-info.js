// README
// スクリプトエディタを起動し
// ミュージックで修正したい曲をマウス等で複数選択し
// このコードを実行する。

app = Application("Music");
app.selection().map((track) => {
	// トラック名の "詳説世界史　" を除去する
	track.name = track.name().replace("詳説世界史　", "");
	return track.name();
});
