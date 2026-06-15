# vllm-project/vllm#8536: [Bug]: Model load on 2 or 4-gpu A100 setup may cause default text encoding to be ascii, unless enforce_eager=True

| 字段 | 值 |
| --- | --- |
| Issue | [#8536](https://github.com/vllm-project/vllm/issues/8536) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model load on 2 or 4-gpu A100 setup may cause default text encoding to be ascii, unless enforce_eager=True

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Loading a model with vllm.LLM on a 2-gpu A100 machine appears to cause the python default file encoding to change from utf-8 to ascii, at least for the Phi-3 and Phi-3.5 MoE models I am loading. This results in a number of strange behaviors, including a requirement for the encoding to be manually specified for python file opens after the model load. In particular, it is easy to see it in action with readline.add_history(...utfcharacters...). I do not see this problem on single-gpu setups. This problem does not occur 100% of the time---rarely everything is OK after model load. In all cases my locale appears to remain a utf-8 locale and sys.getdefaultlocale() reports "utf-8". Enclosed is a program that shows this bug for me: ``` import sys import readline import torch from vllm import LLM readline.add_history("😊") model = LLM( 'Phi-3-medium-128k-instruct', trust_remote_code=True, tensor_parallel_size=torch.cuda.device_count(), ) print(">>> My Current encoding is:", sys.getdefaultencoding()) readline.add_history("😊") # Crashes ``` Here's what the output looks like when I run this: ```text INFO 09-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: el load on 2 or 4-gpu A100 setup may cause default text encoding to be ascii, unless enforce_eager=True bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Loading a model with vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disabl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Model load on 2 or 4-gpu A100 setup may cause default text encoding to be ascii, unless enforce_eager=True bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Loading a mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: an LLM engine (v0.6.1) with config: model='Phi-3-medium-128k-instruct', speculative_config=None, tokenizer='Phi-3-medium-128k-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_con...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
