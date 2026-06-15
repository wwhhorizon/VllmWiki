# vllm-project/vllm#23674: [Bug]: Cannot load model from S3 using RunAI in vllm 0.10.1

| 字段 | 值 |
| --- | --- |
| Issue | [#23674](https://github.com/vllm-project/vllm/issues/23674) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot load model from S3 using RunAI in vllm 0.10.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to load a model from S3 using RunAI streaming in `vllm==0.10.1`, the server fails to start with the following error message: ``` OSError: Can't load the configuration of 's3://BUCKET/mistral'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 's3://BUCKET/mistral' is the correct path to a directory containing a config.json file ``` I have my model files in that s3 directory and it was working before. The major difference I observe is that we bumped from `transformers==4.53.2` to `transfomers=4.55.2`. ## Command ```bash vllm serve s3:// /mistral --host 0.0.0.0 --port 8000 --no-enable-chunked-prefill --enable-prefix-caching --dtype bfloat16 --enable-auto-tool-choice --gpu-memory-utilization 0.95 --load-format runai_streamer --max-model-len 16384 --max-num-seqs 32 --scheduling-policy priority --tool-call-parser mistral ``` ## Environment Variables ``` - name: HF_HUB_OFFLINE value: "1" - name: DO_NOT_TRACK value: "1" - name: VLLM_NO_USAGE_STATS value: "1" - name: AWS_ACCESS_KEY_ID - name: AWS_DEFAULT_REGION - name: AWS_EC...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Cannot load model from S3 using RunAI in vllm 0.10.1 bug ### Your current environment ### 🐛 Describe the bug When trying to load a model from S3 using RunAI streaming in `vllm==0.10.1`, the server fails to start...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: .0.0.0 --port 8000 --no-enable-chunked-prefill --enable-prefix-caching --dtype bfloat16 --enable-auto-tool-choice --gpu-memory-utilization 0.95 --load-format runai_streamer --max-model-len 16384 --max-num-seqs 32 --sche...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: vllm serve s3:// /mistral --host 0.0.0.0 --port 8000 --no-enable-chunked-prefill --enable-prefix-caching --dtype bfloat16 --enable-auto-tool-choice --gpu-memory-utilization 0.95 --load-format runai_streamer --max-model-...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23681: Should have ROCm label: NO (0 matches) #23674: Should have ROCm label: NO (0 matches) #23670: Should have ROCm label: NO (0 matches) #23669: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
