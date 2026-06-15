# vllm-project/vllm#25226: [Installation]: How can I install vllm from source with cuda 124 while system cuda version is higher (129)

| 字段 | 值 |
| --- | --- |
| Issue | [#25226](https://github.com/vllm-project/vllm/issues/25226) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: How can I install vllm from source with cuda 124 while system cuda version is higher (129)

### Issue 正文摘录

### Your current environment I want to install torch 2.6.0 + cuda124, and vllm 0.8.5.post1. Since I made some revisions to vllm source code, so I need to install vllm from source. However, my system cuda version is cuda129, I want to install cuda 124 version is to maintain a same env in another machine where cuda version is 124. And I use following commands to install my revised vllm (mainly to incorporate deepconf): ```bash pip install -r requirements/build.txt pip install --no-build-isolation -e . ``` My env uses python=3.10, and I first installed torch 2.6.0+cuda124, and then install the vllm revised. And error raised like: ```bash Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple Obtaining file:///data/home/xxxxxxxx/workspace/vllm-dev Checking if build backend supports build_editable ... done Preparing editable metadata (pyproject.toml) ... error error: subprocess-exited-with-error × Preparing editable metadata (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [24 lines of output] Traceback (most recent call last): File "/data/home/xxxxxxxx/miniconda3/envs/enb/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: How can I install vllm from source with cuda 124 while system cuda version is higher (129) installation ### Your current environment I want to install torch 2.6.0 + cuda124, and vllm 0.8.5.post1. Since I
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: How can I install vllm from source with cuda 124 while system cuda version is higher (129) installation ### Your current environment I want to install torch 2.6.0 + cuda124, and vllm 0.8.5.post1. Since I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: aining file:///data/home/xxxxxxxx/workspace/vllm-dev Checking if build backend supports build_editable ... done Preparing editable metadata (pyproject.toml) ... error error: subprocess-exited-with-error × Preparing edit...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g if build backend supports build_editable ... done Preparing editable metadata (pyproject.toml) ... error error: subprocess-exited-with-error × Preparing editable metadata (pyproject.toml) did not run successfully. │ e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: re_metadata_for_build_editable return hook(metadata_directory, config_settings) File "/data/home/xxxxxxxx/miniconda3/envs/enb/lib/python3.10/site-packages/setuptools/build_meta.py", line 488, in prepare_metadata_for_bui...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
