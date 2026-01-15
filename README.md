# Git 测试项目

这是一个用于学习和测试 Git 功能的简单项目。

## 项目结构
- `main.py`: 主程序文件
- `utils.py`: 工具函数
- `README.md`: 项目说明
- `.gitignore`: Git 忽略文件

## 如何使用
1. 初始化 Git 仓库：`git init`
2. 添加文件：`git add .`
3. 提交：`git commit -m "Initial commit"`
4. 创建分支：`git branch feature-branch`
5. 切换分支：`git checkout feature-branch`
6. 修改文件并提交
7. 合并分支：`git checkout main && git merge feature-branch`

## 练习任务
- 修改 `main.py` 中的代码
- 创建新文件
- 使用 `git log` 查看历史
- 使用 `git diff` 查看更改
- 练习撤销更改：`git reset` 或 `git revert`