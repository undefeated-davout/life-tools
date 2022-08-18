# README

## 設定方法

```(bash)
# ログイン、ログアウト設定確認
sudo defaults read com.apple.loginwindow

# ログイン設定
sudo defaults write com.apple.loginwindow LoginHook ~/work/repo/github.com/undefeated-davout/life-tools/set-sound/01-middle-sound.sh

# ログアウト設定
sudo defaults write com.apple.loginwindow LogoutHook ~/work/repo/github.com/undefeated-davout/life-tools/set-sound/02-small-sound.sh

# ログアウト設定削除
sudo defaults delete com.apple.loginwindow LogoutHook

# 実行権限付与
sudo chmod +x ~/work/repo/github.com/undefeated-davout/life-tools/set-sound/01-middle-sound.sh ~/work/repo/github.com/undefeated-davout/life-tools/set-sound/02-small-sound.sh
```

## 注意

- Documentディレクトリなど、権限的に実行できないディレクトリもあるので  
  ユーザディレクトリ配下に自分でディレクトリ作成するのが良さそう
