# Git Submodules commands


```shell
git submodule deinit --all -f   
```

```shell
git submodule add -b feature/submodules_demo --name simple-mail2 git@github.com:luiscberrocal/simple-mail.git simple_mail  
```
## Scenarios

### Making changes to submodule in project

Make a change in the submodule and commit it.

### Running ruff
 - 
![lg_git_submodules.png](images%2Flg_git_submodules.png)

Hit enter on `simple_mail` to see the changes in the submodule.

![lg_inside_submodule.png](images%2Flg_inside_submodule.png)

Commit

### Making changes on the submoduled repository




## Issues

- Pycharm does not commit. We commit in lazygit but it doesnot show the changes in Pycharm.

### Cannot commit submodule changes in lazygit

![lg_error_commiting_submodule_changes.png](images%2Flg_error_commiting_submodule_changes.png)

### Workaround

Change `~/.ssh/config` to use the `id_rsa` key for the submodule repository.

The submodule repository is takeing the default.



```shell
Host github.com
        HostName github.com
        User git
        IdentityFile ~/.ssh/github_luis.berrocal.1942
        #IdentitiesOnly yes
Host github.com-payjoy
        HostName github.com
        User git
        IdentityFile ~/.ssh/github_payjoy
        #IdentitiesOnly yes
```
## Pycharm configuration


PyCharm 2023.3.5 (Professional Edition)
Build #PY-233.15026.15, built on March 21, 2024
Subscription is active until March 15, 2025.
Runtime version: 17.0.10+1-b1087.23 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Linux 6.8.0-76060800daily20240311-generic
GC: G1 Young Generation, G1 Old Generation
Memory: 4096M
Cores: 20
Registry:
  ide.experimental.ui=true
Non-Bundled Plugins:
  IdeaVIM (2.11.0)
  com.github.copilot (1.5.2.5345)
  com.koxudaxi.ruff (0.0.33)
  com.leinardi.pycharm.pylint (0.16.2)
  mobi.hsz.idea.gitignore (4.5.3)
Current Desktop: pop:GNOME
