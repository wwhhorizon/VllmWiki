# vllm-project/vllm#41906: [Bug]: `collect_env.py` crashes on non-Linux platforms (macOS/Windows) due to unconditional assert in `get_pkg_version`

| 字段 | 值 |
| --- | --- |
| Issue | [#41906](https://github.com/vllm-project/vllm/issues/41906) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: `collect_env.py` crashes on non-Linux platforms (macOS/Windows) due to unconditional assert in `get_pkg_version`

### Issue 正文摘录

### Your current environment ``` Traceback (most recent call last): File "/Volumes/dev/project/vllm/vllm/collect_env.py", line 1083, in main() File "/Volumes/dev/project/vllm/vllm/collect_env.py", line 1055, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/Volumes/dev/project/vllm/vllm/collect_env.py", line 1050, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "/Volumes/dev/project/vllm/vllm/collect_env.py", line 789, in get_env_info intel_graphics_compiler_version=get_intel_graphics_compiler_version(run_lambda), ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Volumes/dev/project/vllm/vllm/collect_env.py", line 371, in get_intel_graphics_compiler_version return get_pkg_version(run_lambda, "igc") ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Volumes/dev/project/vllm/vllm/collect_env.py", line 304, in get_pkg_version assert get_platform() == "linux" ^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError ``` ### 🐛 Describe the bug After PR #35698 ([XPU]Enhance environment collection for Intel XPU and optimize layout, commit 9dd5ee011), running python collect_env.py on non-Linux platforms (macOS, Windows) crashes with an AssertionError. **Root Caus...

## 现有链接修复摘要

#35698 [XPU]Enhance environment collection for Intel XPU and optimize layout

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -Linux platforms (macOS/Windows) due to unconditional assert in `get_pkg_version` bug ### Your current environment ``` Traceback (most recent call last): File "/Volumes/dev/project/vllm/vllm/collect_env.py", line 1083,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: : return None ... ``` performance ci_build;hardware_porting cuda build_error;crash env_dependency;memory_layout #35698 [XPU]Enhance environment collection for Intel XPU and optimize layout Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: R #35698 ([XPU]Enhance environment collection for Intel XPU and optimize layout, commit 9dd5ee011), running python collect_env.py on non-Linux platforms (macOS, Windows) crashes with an AssertionError. **Root Cause:** T...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35698](https://github.com/vllm-project/vllm/pull/35698) | mentioned | 0.45 | [XPU]Enhance environment collection for Intel XPU and optimize layout | ^^^^^^^^^^^^^^ assertionerror ``` ### 🐛 describe the bug after pr #35698 ([xpu]enhance environment collection for intel xpu and optimize layout, commit 9dd5ee011), running python… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
