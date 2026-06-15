# vllm-project/vllm#2325: [ERROR] [ -4263953,Not implemented in the current version ] nvmlDeviceGetHandleByPciBusId() This is unlikely to affect the main functionalities of user applications.

| 字段 | 值 |
| --- | --- |
| Issue | [#2325](https://github.com/vllm-project/vllm/issues/2325) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [ERROR] [ -4263953,Not implemented in the current version ] nvmlDeviceGetHandleByPciBusId() This is unlikely to affect the main functionalities of user applications.

### Issue 正文摘录

when i run this command: ``` llm = LLM(model="qwen/Qwen-7B-Chat", revision="v1.1.8", trust_remote_code=True,quantization='awq') ``` the error below: ``` WARNING 01-03 11:47:54 config.py:171] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 01-03 11:47:54 llm_engine.py:73] Initializing an LLM engine with config: model='/data/share/rwq/Qwen-7B-Chat', tokenizer='/data/share/rwq/Qwen-7B-Chat', tokenizer_mode=auto, revision=v1.1.8, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) WARNING 01-03 11:47:54 tokenizer.py:79] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. 2024-01-03 11:48:06 [ERROR] [ -4263953,Not implemented in the current version ] nvmlDeviceGetHandleByPciBusId() This is unlikely to affect the main functionalities of user applications. ``` how to solve?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tionalities of user applications. when i run this command: ``` llm = LLM(model="qwen/Qwen-7B-Chat", revision="v1.1.8", trust_remote_code=True,quantization='awq') ``` the error below: ``` WARNING 01-03 11:47:54 config.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LLM(model="qwen/Qwen-7B-Chat", revision="v1.1.8", trust_remote_code=True,quantization='awq') ``` the error below: ``` WARNING 01-03 11:47:54 config.py:171] awq quantization is not fully optimized yet. The speed can be s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [ERROR] [ -4263953,Not implemented in the current version ] nvmlDeviceGetHandleByPciBusId() This is unlikely to affect the main functionalities of user applications. when i run this command: ``` llm = LLM(model="qwen/Qw...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
