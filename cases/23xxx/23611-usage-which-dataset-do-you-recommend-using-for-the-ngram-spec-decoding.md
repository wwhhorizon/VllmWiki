# vllm-project/vllm#23611: [Usage]: Which dataset do you recommend using for the ngram spec decoding method?

| 字段 | 值 |
| --- | --- |
| Issue | [#23611](https://github.com/vllm-project/vllm/issues/23611) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cache;fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Which dataset do you recommend using for the ngram spec decoding method?

### Issue 正文摘录

### Your current environment Hi team, Please find below my methodology. Pull Docker Image docker pull vllm/vllm-openai:latest Run vLLM Docker Container docker run -d \ --gpus all \ --name vllm-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.3-70B-Instruct \ --tensor-parallel-size 8 \ --kv-cache-dtype fp8 \ --quantization fp8 \ --speculative-config '{ "method": "ngram", "num_speculative_tokens": 2 }' \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 Run vLLM Benchmark sudo docker exec vllm-8b-bf16-h100 vllm bench serve \ --backend vllm \ --num-prompts 2 \ --dataset-name random \ --model meta-llama/Llama-3.1-8B-Instruct \ --random-input-len 1000 \ --random-output-len 100 \ --seed 3 \ --random-range-ratio 0.0 \ --host localhost \ --port 8000 \ --percentile-metrics ttft,tpot,itl,e2el \ --metric-percentiles 25,50,90,95,99 \ --save-result \ --append-result \ --result-dir ./benchmark_results \ --result-filename results_8b_bf16_h100.json I'm doing the above for many models and also default quantization but wanted to give an example where I use kv cache as fp 8. I'm benchmarking across num_prompts from {1,2,4..1024} and input {10...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: --gpus all \ --name vllm-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.3-70B-Instruct \ --tensor-parallel-size 8 \ --kv-cache-dtype fp8 \ --quantization fp8 \...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: llama/Llama-3.3-70B-Instruct \ --tensor-parallel-size 8 \ --kv-cache-dtype fp8 \ --quantization fp8 \ --speculative-config '{ "method": "ngram", "num_speculative_tokens": 2 }' \ --trust-remote-code \ --host 0.0.0.0 \ --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Run vLLM Docker Container docker run -d \ --gpus all \ --name vllm-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vllm/vllm-openai:latest \ --model meta-llama/Llama-3.3-70B-Instruct \ --tensor-parallel-size 8 \ --...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: below my methodology. Pull Docker Image docker pull vllm/vllm-openai:latest Run vLLM Docker Container docker run -d \ --gpus all \ --name vllm-b200 \ -p 8000:8000 \ --ipc=host \ -e HF_TOKEN=... \ vllm/vllm-openai:latest...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: current environment Hi team, Please find below my methodology. Pull Docker Image docker pull vllm/vllm-openai:latest Run vLLM Docker Container docker run -d \ --gpus all \ --name vllm-b200 \ -p 8000:8000 \ --ipc=host \...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | ot custom compiler extension via CompilerI... [feature request] 12. #23611: [Usage]: Which dataset do you recommend using for the ngram ... [usage] 13. #23610: [Feature]: Add LoRA… |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23612: Should have ROCm label: NO (0 matches) #23611: Should have ROCm label: NO (0 matches) #23610: Should have ROCm label: NO (0 matches) #23609: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
