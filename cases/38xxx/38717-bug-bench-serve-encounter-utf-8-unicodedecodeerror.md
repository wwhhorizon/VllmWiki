# vllm-project/vllm#38717: [Bug]: Bench Serve encounter utf-8 UnicodeDecodeError

| 字段 | 值 |
| --- | --- |
| Issue | [#38717](https://github.com/vllm-project/vllm/issues/38717) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bench Serve encounter utf-8 UnicodeDecodeError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Serve GLM-4.7-FP8 with: ```bash vllm serve zai-org/GLM-4.7-FP8 \ --tensor-parallel-size 8 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --async-scheduling \ --enable-prefix-caching \ --max-num-batched-tokens 4K ``` Run Bench serve in another terminal ```bash vllm bench serve \ --model zai-org/GLM-4.7-FP8 \ --port 8000 \ --save-result \ --save-detailed \ --backend=vllm \ --dataset-name random \ --disable-shuffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics "ttft,tpot,e2el" \ --result-dir "./vllm_bench_results/test/" \ --request-rate 1 \ --random-input-len 40000 \ --random-output-len 300 ``` Got results with 4 `UnicodeDecodeError`: ```bash Namespace(subparser='bench', bench_type='serve', dispatch_function= , trust_remote_code=False, seed=0, num_prompts=1000, dataset_name='random', no_stream=False, dataset_path=None, no_oversample=False, skip_chat_template=False, enable_multimodal_chat=False, disable_shuffle=True, custom_output_len=256, spec_bench_output_len=256, spec_bench_category=None, sonnet_inpu...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: huffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics "ttft,tpot,e2el" \ --result-dir "./vllm_bench_results/test/" \ --request-rate 1 \ --random-input-len 40000 \ --random-output-len 300 ``` Got results wit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Bench Serve encounter utf-8 UnicodeDecodeError bug ### Your current environment ### 🐛 Describe the bug Serve GLM-4.7-FP8 with: ```bash vllm serve zai-org/GLM-4.7-FP8 \ --tensor-parallel-size 8 \ --speculative-con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: he default will be determined on the server side and can be model/API specific. For the old behavior, include --temperature=0. Starting initial single prompt test run... Skipping endpoint ready check. Starting main benc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: llm serve zai-org/GLM-4.7-FP8 \ --tensor-parallel-size 8 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choic...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: zai-org/GLM-4.7-FP8 \ --port 8000 \ --save-result \ --save-detailed \ --backend=vllm \ --dataset-name random \ --disable-shuffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics "ttft,tpot,e2el" \ --result-di...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
