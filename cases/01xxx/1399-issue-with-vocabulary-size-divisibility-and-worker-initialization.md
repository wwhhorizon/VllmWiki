# vllm-project/vllm#1399: Issue with Vocabulary Size Divisibility and Worker Initialization

| 字段 | 值 |
| --- | --- |
| Issue | [#1399](https://github.com/vllm-project/vllm/issues/1399) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue with Vocabulary Size Divisibility and Worker Initialization

### Issue 正文摘录

Hello vLLM team and community, First and foremost, thanks for all your hard work and dedication on this project. **Issue Description:** I've encountered an issue while trying to run inference for ehartford/WizardLM-Uncensored-Falcon-40b. The main problem seems to revolve around the vocabulary size (`65025`) not being divisible by the number of workers (`4`). ```python python -m vllm.entrypoints.openai.api_server \ --model ehartford/WizardLM-Uncensored-Falcon-40b --tensor-parallel-size 4 --host 0.0.0.0 --port 8080 --trust-remote-code ``` Here's the traceback I received: ```plaintext ` Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/openai/api_server.py", line 616, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 486, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py"...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s (`4`). ```python python -m vllm.entrypoints.openai.api_server \ --model ehartford/WizardLM-Uncensored-Falcon-40b --tensor-parallel-size 4 --host 0.0.0.0 --port 8080 --trust-remote-code ``` Here's the traceback I recei...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 60, "parallel_attn": true, "torch_dtype": "float16", "transformers_version": "4.28.1", "use_cache": true, "vocab_size": 65025 } ``` I'm also seeing these warnings one of which may be relevant and the other which is like...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 28, "n_head_kv": 8, "n_layer": 60, "parallel_attn": true, "torch_dtype": "float16", "transformers_version": "4.28.1", "use_cache": true, "vocab_size": 65025 } ``` I'm also seeing these warnings one of which may be relev...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: "alibi": false, "apply_residual_connection_post_layernorm": false, "architectures": [ "RWForCausalLM" ], "attention_dropout": 0.0, "auto_map": { "AutoConfig": "configuration_RW.RWConfig", "AutoModelForCausalLM": "modell...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: name_or_path": "/workspace/WizardLM-Uncensored-falcon-40b", "alibi": false, "apply_residual_connection_post_layernorm": false, "architectures": [ "RWForCausalLM" ], "attention_dropout": 0.0, "auto_map": { "AutoConfig":...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
