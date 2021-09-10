# proxy
function proxy() {
	export http_proxy=http://127.0.0.1:8889
	export https_proxy=http://127.0.0.1:8889
}

function unproxy() {
	unset http_proxy
	unset https_proxy
}

# clean
function clean() {
	# npm cache clean --force
	vim -c 'CocCommand yank.clean' -c 'qa!'

	# history
	rm ~/.zsh_history
	rm ~/.bash_history
	rm ~/.mysql_history
	rm ~/.python_history
	rm ~/.rediscli_history
	rm ~/.node_repl_history

	# cache
	rm ~/.vuerc
	rm ~/.cache
	rm ~/.config/nvim/tmp

	# rm -rf ~/.local/trash
	rm --clean
}

