# vllm-project/vllm#7430: [Bug]: Does not work on MacOS

| 字段 | 值 |
| --- | --- |
| Issue | [#7430](https://github.com/vllm-project/vllm/issues/7430) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Does not work on MacOS

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The instructions on the front page don't seem to work for MacOS. I'm at a loss for what to do next. ` pip install vllm ` ``` Defaulting to user installation because normal site-packages is not writeable Collecting vllm Downloading vllm-0.5.4.tar.gz (958 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 958.6/958.6 kB 2.8 MB/s eta 0:00:00 Installing build dependencies ... error error: subprocess-exited-with-error × pip subprocess to install build dependencies did not run successfully. │ exit code: 1 ╰─> [10 lines of output] Collecting cmake>=3.21 Downloading cmake-3.30.2-py3-none-macosx_11_0_universal2.macosx_10_10_x86_64.macosx_11_0_arm64.whl.metadata (6.1 kB) Collecting ninja Downloading ninja-1.11.1.1-py2.py3-none-macosx_10_9_universal2.macosx_10_9_x86_64.macosx_11_0_arm64.macosx_11_0_universal2.whl.metadata (5.3 kB) Collecting packaging Using cached packaging-24.1-py3-none-any.whl.metadata (3.2 kB) Collecting setuptools>=49.4.0 Downloading setuptools-72.1.0-py3-none-any.whl.metadata (6.6 kB) ERROR: Could not find a version that satisfies the requirement torch==2.4.0 (from versions: 1.7.1, 1.8.0, 1.8.1, 1.9.0, 1.9.1, 1.10.0, 1.10.1,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: don't seem to work for MacOS. I'm at a loss for what to do next. ` pip install vllm ` ``` Defaulting to user installation because normal site-packages is not writeable Collecting vllm Downloading vllm-0.5.4.tar.gz (958...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ikely not a problem with pip. ``` development ci_build;hardware_porting cuda build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: y3-none-macosx_11_0_universal2.macosx_10_10_x86_64.macosx_11_0_arm64.whl.metadata (6.1 kB) Collecting ninja Downloading ninja-1.11.1.1-py2.py3-none-macosx_10_9_universal2.macosx_10_9_x86_64.macosx_11_0_arm64.macosx_11_0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Does not work on MacOS bug;stale ### Your current environment ### 🐛 Describe the bug The instructions on the front page don't seem to work for MacOS. I'm at a loss for what to do next. ` pip install vllm ` ``` De...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
