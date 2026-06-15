# vllm-project/vllm#199: Add support for H100

| 字段 | 值 |
| --- | --- |
| Issue | [#199](https://github.com/vllm-project/vllm/issues/199) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Add support for H100

### Issue 正文摘录

Thanks for the repo! I can build the repo successfully on H100 machine. But when I run the benchmarks, it shows the error below: ``` FATAL: kernel `fmha_cutlassF_f16_aligned_64x128_rf_sm80` is for sm80-sm100, but was built for sm50 ``` which will further cause the issue: ``` Traceback (most recent call last): File "benchmark_latency.py", line 77, in main(args) File "benchmark_latency.py", line 57, in main latencies.append(run_to_completion(profile=False)) File "benchmark_latency.py", line 41, in run_to_completion llm.generate(prompt_token_ids=dummy_prompt_token_ids, File "/home/ubuntu/vllm/vllm/entrypoints/llm.py", line 114, in generate return self._run_engine(use_tqdm) File "/home/ubuntu/vllm/vllm/entrypoints/llm.py", line 134, in _run_engine step_outputs = self.llm_engine.step() File "/home/ubuntu/vllm/vllm/engine/llm_engine.py", line 225, in step output = self._run_workers( File "/home/ubuntu/vllm/vllm/engine/llm_engine.py", line 307, in _run_workers output = executor(*args, **kwargs) File "/home/ubuntu/anaconda3/envs/cacheflow/lib/python3.8/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/home/ubuntu/vllm/vllm/worker/...

## 现有链接修复摘要

#26188 [CI Bugfix] Make sure TRTLLM attention is available in test_blackwell_moe | #26959 [Bugfix] Fix Marlin incompatibility on ROCM | #26978 [CI/Build] Update expected beam search output for Phi3V

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: Add support for H100 bug Thanks for the repo! I can build the repo successfully on H100 machine. But when I run the benchmarks, it shows the error below: ``` FATAL: kernel `fmha_cutlassF_f16_aligned_64x128_rf_sm80` is f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Add support for H100 bug Thanks for the repo! I can build the repo successfully on H100 machine. But when I run the benchmarks, it shows the error below: ``` FATAL: kernel `fmha_cutlassF_f16_aligned_64x128_rf_sm80` is f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: o! I can build the repo successfully on H100 machine. But when I run the benchmarks, it shows the error below: ``` FATAL: kernel `fmha_cutlassF_f16_aligned_64x128_rf_sm80` is for sm80-sm100, but was built for sm50 ``` w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: I run the benchmarks, it shows the error below: ``` FATAL: kernel `fmha_cutlassF_f16_aligned_64x128_rf_sm80` is for sm80-sm100, but was built for sm50 ``` which will further cause the issue: ``` Traceback (most recent c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: latencies.append(run_to_completion(profile=False)) File "benchmark_latency.py", line 41, in run_to_completion llm.generate(prompt_token_ids=dum

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26188](https://github.com/vllm-project/vllm/pull/26188) | mentioned | 0.6 | [CI Bugfix] Make sure TRTLLM attention is available in test_blackwell_moe | /ci/builds/33421/steps/canvas?sid=0199aac3-cb53-4c8f-a99b-7f24c012fae3#0199aac3-cb53-4c8f-a99b-7f24c012fae3/58-499 ## Test Plan ## Test Result --- <details> <summary> Essential El… |
| [#26959](https://github.com/vllm-project/vllm/pull/26959) | mentioned | 0.6 | [Bugfix] Fix Marlin incompatibility on ROCM  | --tp-size=1 ``` 2. AMD CI([before](https://buildkite.com/vllm/ci/builds/35119#0199ea4c-05fd-4da8-9812-6dec9c6bfce0)) ``` =========================== short test summary info ======… |
| [#26978](https://github.com/vllm-project/vllm/pull/26978) | closes_keyword | 0.95 | [CI/Build] Update expected beam search output for Phi3V | FIX https://buildkite.com/vllm/ci/builds/35110#0199ea1c-8eae-4fb8-b8a5-e936be422cd3 Probably caused by updates to the kernels, the output is still reasonable ## Test Plan ## Tes |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
