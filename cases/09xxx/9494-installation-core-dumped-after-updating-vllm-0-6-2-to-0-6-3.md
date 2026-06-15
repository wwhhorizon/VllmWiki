# vllm-project/vllm#9494: [Installation]: Core dumped after updating vllm 0.6.2 to 0.6.3 

| 字段 | 值 |
| --- | --- |
| Issue | [#9494](https://github.com/vllm-project/vllm/issues/9494) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Core dumped after updating vllm 0.6.2 to 0.6.3 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to update vllm 0.6.2 to 0.6.3. Followed by https://docs.vllm.ai/en/latest/getting_started/installation.html, I run ```python python_only_dev.py --quit-dev``` but got an error. So I run ```pip uninstall vllm```, ```pip install https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl```+clone the latest code + ```python python_only_dev.py```. After that, I tried to run the demo vllm code but got "**Aborted (core dumped)**“. I rebuilt my conda env, and the "core dumped" error disappeared. **However, I got a NCCL error:** ``` INFO 10-18 14:42:48 utils.py:1009] Found nccl from library libnccl.so.2 ERROR 10-18 14:42:48 pynccl_wrapper.py:196] Failed to load NCCL library from libnccl.so.2 .It is expected if you are not running on NVIDIA/AMD GPUs.Otherwise, the nccl library might not exist, be corrupted or it does not support the current platform Linux-5.15.0-50-generic-x86_64-with-glibc2.31.If you already have the library, please set the environment variable VLLM_NCCL_SO_PATH to point to the correct nccl library path. ``` Then I check my driver by run...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: Core dumped after updating vllm 0.6.2 to 0.6.3 installation ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to update vllm 0.6.2 to 0.6.3. Followed by
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the correct nccl library path. ``` Then I check my driver by running ```CUDA_VISIBLE_DEVICES=6,7 NCCL_DEBUG=TRACE torchrun --nproc-per-node=2 test_vllm_env.py```. It seems that NCCL is not found. Indeed, **I checked thi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g vllm 0.6.2 to 0.6.3 installation ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to update vllm 0.6.2 to 0.6.3. Followed by https://docs.vllm.ai/en/latest/getting_started...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
