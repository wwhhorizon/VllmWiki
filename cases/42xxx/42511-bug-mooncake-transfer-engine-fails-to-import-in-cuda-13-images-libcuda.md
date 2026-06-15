# vllm-project/vllm#42511: [Bug]: mooncake-transfer-engine fails to import in CUDA 13 images: libcudart.so.12 missing

| 字段 | 值 |
| --- | --- |
| Issue | [#42511](https://github.com/vllm-project/vllm/issues/42511) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mooncake-transfer-engine fails to import in CUDA 13 images: libcudart.so.12 missing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start vllm with `vllm serve xxxx --kv-transfer-config '{"kv_connector":"MooncakeConnector","kv_role":"kv_both"}'`, it reports ` [mooncake_connector.py:61] Please install mooncake by following the instructions at https://github.com/kvcache-ai/Mooncake/blob/main/doc/en/build.md to run VLLM with MooncakeTransferEngine.` ``` # python3 Python 3.12.13 (main, May 8 2026, 20:13:12) [GCC 11.4.0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> from mooncake.engine import TransferEngine Traceback (most recent call last): File " ", line 1, in ImportError: libcudart.so.12: cannot open shared object file: No such file or directory ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: mooncake-transfer-engine fails to import in CUDA 13 images: libcudart.so.12 missing bug ### Your current environment ### 🐛 Describe the bug start vllm with `vllm serve xxxx --kv-transfer-config '{"kv_connector":"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: mooncake-transfer-engine fails to import in CUDA 13 images: libcudart.so.12 missing bug ### Your current environment ### 🐛 Describe the bug start vllm with `vllm serve xxxx --kv-transfer-config '{"kv_connector":"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug start vllm with `vllm serve xxxx --kv-transfer-config '{"kv_connector":"MooncakeConnector","kv_role":"kv_both"}'`, it reports ` [mooncake_connector.py:61] Please install mooncake by following the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel cuda build_error;crash;i...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
