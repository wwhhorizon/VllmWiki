# vllm-project/vllm#22467: [Bug]: Dependencies versions not pinned in tools/ep_kernels/install_python_libraries.sh

| 字段 | 值 |
| --- | --- |
| Issue | [#22467](https://github.com/vllm-project/vllm/issues/22467) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dependencies versions not pinned in tools/ep_kernels/install_python_libraries.sh

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The libraries installed in [tools/ep_kernels/install_python_libraries.sh](https://github.com/vllm-project/vllm/blob/7e3a8dc90670fd312ce1e0d4eba9bf11c571e3ad/tools/ep_kernels/install_python_libraries.sh#L14) don't have a pinned version, which is causing some compatibility issues between torch and torchvision. ``` Traceback (most recent call last): File "/opt/dynamo/venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2292, in __getattr__ module = self._get_module(self._class_to_module[name]) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/dynamo/venv/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 2322, in _get_module ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/dynamo/venv/lib/python3.12/site-packages/torch/library.py", line 1069, in register use_lib._register_fake( File "/opt/dynamo/venv/lib/python3.12/site-packages/torch/library.py", line 219, in _register_fake handle = entry.fake_impl.register( ^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/dynamo/venv/lib/python3.12/site-packages/torch/_library/fake_impl.py", line 50, in register if torch._C._dispatch_has_kernel_for_d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Dependencies versions not pinned in tools/ep_kernels/install_python_libraries.sh bug ### Your current environment ### 🐛 Describe the bug The libraries installed in [tools/ep_kernels/install_python_libraries.sh](h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ages/torch/_library/fake_impl.py", line 50, in register if torch._C._dispatch_has_kernel_for_dispatch_key(self.qualname, "Meta"): ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ RuntimeError: opera...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: or v0.10.0, torch version is pinned to 2.7.1, but here it installs the latest, which is 2.8.0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
