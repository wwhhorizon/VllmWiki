# vllm-project/vllm#359: The A100 test performance did not match the official test results

| 字段 | 值 |
| --- | --- |
| Issue | [#359](https://github.com/vllm-project/vllm/issues/359) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The A100 test performance did not match the official test results

### Issue 正文摘录

I install vllm with ```shell pip install vllm ``` then use that command start server ```shell CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.api_server --model llama-7b-hf/ --swap-space 16 --disable-log-requests --port 9009 ``` benchmark with that ```shell python benchmark_serving.py --backend vllm --tokenizer ./llama-7b-hf/ --dataset ShareGPT_V3_unfiltered_cleaned_split.json --request-rate 200 --host 127.0.0.1 --port 9009 ``` output: ```shell Namespace(backend='vllm', best_of=1, dataset='ShareGPT_V3_unfiltered_cleaned_split.json', host='127.0.0.1', num_prompts=1000, port=9009, request_rate=200.0, seed=0, tokenizer='/data/zhaohb/llama-7b-hf/', use_beam_search=False) Token indices sequence length is longer than the specified maximum sequence length for this model (3152 > 2048). Running this sequence through the model will result in indexing errors Total time: 166.88 s Throughput: 5.99 requests/s Average latency: 67.59 s Average latency per token: 0.21 s Average latency per output token: 1.10 s ``` This is far from official, how to fix that? Moreover, I used benchmark_throughput.py test, and the performance was also very different: ```shell python benchmark_throughput.py --model...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```shell CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.api_server --model llama-7b-hf/ --swap-space 16 --disable-log-requests --port 9009 ``` benchmark with that ```shell python benchmark_serving.py --backend vllm -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: The A100 test performance did not match the official test results I install vllm with ```shell pip install vllm ``` then use that command start server ```shell CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.api_serve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: The A100 test performance did not match the official test results I install vllm with ```shell pip install vllm ``` then use that command start server ```shell CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.api_serve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: The A100 test performance did not match the official test results I install vllm with ```shell pip install vllm ``` then use that command start server ```shell CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.api_serve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: nitializing an LLM engine with config: model='/data/zhaohb/llama-7b-hf', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 07-04 09:54:21 tokeniz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
