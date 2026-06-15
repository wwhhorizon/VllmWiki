# vllm-project/vllm#19195: [Bug]: InternVL2_5-8B-AWQ has no any throughput benefit  compared to the InternVL2_5-8B

| 字段 | 值 |
| --- | --- |
| Issue | [#19195](https://github.com/vllm-project/vllm/issues/19195) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL2_5-8B-AWQ has no any throughput benefit  compared to the InternVL2_5-8B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run the InternVL2_5-8B by ``` vllm serve InternVL/InternVL2_5-8B \ --disable-log-request \ --trust_remote_code \ --port 20010 \ --host 0.0.0.0 ``` And run the benchmark by ``` python3 vllm/benchmarks/benchmark_serving.py \ --model InternVL/InternVL2_5-8B \ --backend openai-chat \ --endpoint /v1/chat/completions \ --dataset-name hf \ --dataset-path lmms-lab/LLaVA-OneVision-Data \ --hf-split train \ --hf-subset "CLEVR-Math(MathV360K)" \ --num-prompts 1000 \ --trust_remote_code \ --host 0.0.0.0 \ --port 20010 \ --max-concurrency 100 ``` The benchmark output is: ``` Namespace(backend='openai-chat', base_url=None, host='0.0.0.0', port=20010, endpoint='/v1/chat/completions', dataset_name='hf', dataset_path='lmms-lab/LLaVA-OneVision-Data', max_concurrency=100, model='InternVL/InternVL2_5-8B', tokenizer=None, use_beam_search=False, num_prompts=1000, logprobs=None, request_rate=inf, burstiness=1.0, seed=0, trust_remote_code=True, disable_tqdm=False, profile=False, save_result=False, save_detailed=False, append_result=False, metadata=None, result_dir=None, result_filename=None, ignore_eos=False, percentile_metrics='ttft,tpot,itl', metric...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: InternVL2_5-8B-AWQ has no any throughput benefit compared to the InternVL2_5-8B bug;stale ### Your current environment ### 🐛 Describe the bug I run the InternVL2_5-8B by ``` vllm serve InternVL/InternVL2_5-8B \ -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: InternVL2_5-8B-AWQ has no any throughput benefit compared to the InternVL2_5-8B bug;stale ### Your current environment ### 🐛 Describe the bug I run the InternVL2_5-8B by ``` vllm serve InternVL/InternVL2_5-8B \
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits cuda;operator;quantization;s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /benchmark_serving.py \ --model InternVL/InternVL2_5-8B \ --backend openai-chat \ --endpoint /v1/chat/completions \ --dataset-name hf \ --dataset-path lmms-lab/LLaVA-OneVision-Data \ --hf-split train \ --hf-subset "CLEV...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ternVL2_5-8B-AWQ by ``` vllm serve InternVL/InternVL2_5-8B-AWQ \ --quantization awq \ --dtype="half" \ --disable-log-request \ --trust_remote_code \ --port 20010 \ --host 0.0.0.0 ``` And run the benchmark by ``` python3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
