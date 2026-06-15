# vllm-project/vllm#7907: [Bug]: Unable to use speculative decoding (KeyError: 40)

| 字段 | 值 |
| --- | --- |
| Issue | [#7907](https://github.com/vllm-project/vllm/issues/7907) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to use speculative decoding (KeyError: 40)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm not able to use speculative decoding whatever the method is. Downgrading to previous vllm version doesn't fix the issue. ```bash python -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --model models/Meta-Llama-3.1-70B-Instruct-FP8 \ --dtype "auto" \ --port 8000 \ --seed 123 \ --max-model-len 32768 \ --gpu-memory-utilization 0.92 \ --tensor-parallel-size 4 \ --max-num-seqs 32 \ --use-v2-block-manager \ --max-log-len 20 \ --served-model-name llama \ --speculative_model "[ngram]" \ --num_speculative_tokens 5 \ --ngram_prompt_lookup_max 8 \ --ngram_prompt_lookup_min 1 ``` Engine starts: ``` INFO 08-27 01:18:22 api_server.py:144] Multiprocessing frontend to use ipc:///tmp/181452bd-e5ed-43fd-9b35-da2bf817442d for RPC Path. INFO 08-27 01:18:22 api_server.py:161] Started engine process with PID 267269 WARNING 08-27 01:18:24 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead. See https://pypi.org/project/pynvml for more information. INFO 08-27 01:18:27 config.py:813] Defaulting to use mp for distributed inference INFO 08-27 01:18:27 llm_engine.py:184] Initializing an LLM engine (...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Unable to use speculative decoding (KeyError: 40) bug ### Your current environment ### 🐛 Describe the bug I'm not able to use speculative decoding whatever the method is. Downgrading to previous vllm version does...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: peculative decoding whatever the method is. Downgrading to previous vllm version doesn't fix the issue. ```bash python -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --model models/Meta-Llama-3.1-70B-Instru...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: er \ --host 0.0.0.0 \ --model models/Meta-Llama-3.1-70B-Instruct-FP8 \ --dtype "auto" \ --port 8000 \ --seed 123 \ --max-model-len 32768 \ --gpu-memory-utilization 0.92 \ --tensor-parallel-size 4 \ --max-num-seqs 32 \ -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: on -u -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --model models/Meta-Llama-3.1-70B-Instruct-FP8 \ --dtype "auto" \ --port 8000 \ --seed 123 \ --max-model-len 32768 \ --gpu-memory-utilization 0.92 \ --tenso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: er.py:161] Started engine process with PID 267269 WARNING 08-27 01:18:24 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead. See https://pypi.org/project/pynvml for more infor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
