# vllm-project/vllm#6509: [Usage]: No chat template provided. Chat API will not work. How do I get vllm to support Codellama-34B in openai format?

| 字段 | 值 |
| --- | --- |
| Issue | [#6509](https://github.com/vllm-project/vllm/issues/6509) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: No chat template provided. Chat API will not work. How do I get vllm to support Codellama-34B in openai format?

### Issue 正文摘录

### Your current environment How do I get vllm to support Codellama-34B in openai format? I run TheBloke/CodeLlama-34B-Instruct-AWQ in vllm, but it show 'No chat template provided. Chat API will not work.'. And it gives a 404 error when accessed in openai url format. But, I run TheBloke/CodeLlama-13B-Instruct-AWQ is normal. It work fine. the output is ``` INFO 07-17 21:58:12 model_runner.py:173] Loading model weights took 17.0560 GB INFO 07-17 21:58:21 gpu_executor.py:119] # GPU blocks: 655, # CPU blocks: 1365 INFO 07-17 21:58:23 model_runner.py:976] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI. INFO 07-17 21:58:23 model_runner.py:980] CUDA graphs can take additional 1~3 GiB memory per GPU. If you are running out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage. INFO 07-17 21:58:35 model_runner.py:1057] Graph capturing finished in 12 secs. WARNING 07-17 21:58:35 serving_chat.py:347] No chat template provided. Chat API will no...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: plate provided. Chat API will not work. How do I get vllm to support Codellama-34B in openai format? usage ### Your current environment How do I get vllm to support Codellama-34B in openai format? I run TheBloke/CodeLla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ning out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage. INFO 07-17 21:58:35 model_runner.py:1057] Graph captur...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ow how to integrate it with vllm. performance frontend_api;model_support;quantization cuda;quantization oom Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s: 1365 INFO 07-17 21:58:23 model_runner.py:976] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: m. performance frontend_api;model_support;quantization cuda;quantization oom Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
