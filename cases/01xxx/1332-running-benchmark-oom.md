# vllm-project/vllm#1332: running benchmark OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#1332](https://github.com/vllm-project/vllm/issues/1332) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> running benchmark OOM

### Issue 正文摘录

Hi, I'm using 2*3090, the start command is CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.api_server --model Llama-2-7b-chat-hf/ --swap-space 16 --disable-log-requests --port 9009 Then I use python benchmark_serving.py --backend vllm --tokenizer ../../Llama-2-7b-chat-hf/ --dataset ../../ShareGPT_V3_unfiltered_cleaned_split.json --request-rate 200 --host 127.0.0.1 --port 9009 It was able to finish the benchmark. However for the other two benchmarks, python benchmark_latency.py --model ../../Llama-2-7b-chat-hf/ --batch-size 10 --input-len 500 and python benchmark_throughput.py --backend vllm --model ../../Llama-2-7b-chat-hf/ --dataset ../../ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 1, I get OOM: (fastchat) nlp@nlp-1:~/Desktop/20231012_deploy/vllm-main/benchmarks$ python benchmark_throughput.py --backend vllm --model ../../Llama-2-7b-chat-hf/ --dataset ../../ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 1 Namespace(backend='vllm', dataset='../../ShareGPT_V3_unfiltered_cleaned_split.json', model='../../Llama-2-7b-chat-hf/', tokenizer='../../Llama-2-7b-chat-hf/', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=1, seed=0, hf_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ommand is CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.api_server --model Llama-2-7b-chat-hf/ --swap-space 16 --disable-log-requests --port 9009 Then I use python benchmark_serving.py --backend vllm --tokenizer ../...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: running benchmark OOM Hi, I'm using 2*3090, the start command is CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.api_server --model Llama-2-7b-chat-hf/ --swap-space 16 --disable-log-requests --port 9009 Then I use pyt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: either: - Avoid using `tokenizers` before the fork if possible - Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false) Traceback (most recent call last): File "/home/nlp/Desktop/20231012_deploy/v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: odel='../../Llama-2-7b-chat-hf/', tokenizer='../../Llama-2-7b-chat-hf/', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=1, seed=0, hf_max_batch_size=None, trust_remote_code=False, dty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: running benchmark OOM Hi, I'm using 2*3090, the start command is CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.api_server --model Llama-2-7b-chat-hf/ --swap-space 16 --disable-log-requests --port 9009 Then I use pyt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
