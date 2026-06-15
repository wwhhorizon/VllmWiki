# vllm-project/vllm#39490: [Bug]: Multi-LoRA Initialization Failure on Cloud TPU v6e-4 (AssertionError: LoRA is not enabled)

| 字段 | 值 |
| --- | --- |
| Issue | [#39490](https://github.com/vllm-project/vllm/issues/39490) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multi-LoRA Initialization Failure on Cloud TPU v6e-4 (AssertionError: LoRA is not enabled)

### Issue 正文摘录

### Description When attempting to serve a model with Multi-LoRA enabled on Cloud TPU v6e-4 using the latest `vllm/vllm-tpu:latest` image, the EngineCore fails to initialize. The API server correctly parses the LoRA modules, but the underlying TPU JAX worker (EngineCore) crashes with an `AssertionError: LoRA is not enabled` during the graph capture phase. ### Environment * **Hardware:** Cloud TPU v6e-4 (4 chips) * **vLLM Image:** `vllm/vllm-tpu:latest` (v0.13.0) * **Model:** `Qwen/Qwen3-4B-Instruct-2507` * **TP Size:** 4 * **Engine:** V1 (TPU native JAX backend) ### Reproduction ```bash vllm serve Qwen/Qwen3-4B-Instruct-2507 \ --tensor-parallel-size 4 \ --dtype bfloat16 \ --enable-lora \ --max-loras 3 \ --max-lora-rank 64 \ --lora-modules \ adapter1=voidful/llm-codec-fisher-no-init \ adapter2=voidful/auv-codec-librispeech \ adapter3=voidful/unicodec-fisher ``` ### Error Stack ```text (EngineCore_DP0 pid=305) ERROR 04-02 07:26:44 [core.py:866] AssertionError: LoRA is not enabled (EngineCore_DP0 pid=305) Traceback (most recent call last): (EngineCore_DP0 pid=305) File "/workspace/tpu_inference/tpu_inference/worker/tpu_worker.py", line 369, in compile_or_warm_up_model (EngineCore_DP0...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: serve Qwen/Qwen3-4B-Instruct-2507 \ --tensor-parallel-size 4 \ --dtype bfloat16 \ --enable-lora \ --max-loras 3 \ --max-lora-rank 64 \ --lora-modules \ adapter1=voidful/llm-codec-fisher-no-init \ adapter2=voidful/auv-co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: onError: LoRA is not enabled) ### Description When attempting to serve a model with Multi-LoRA enabled on Cloud TPU v6e-4 using the latest `vllm/vllm-tpu:latest` image, the EngineCore fails to initialize. The API server...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: wen3-4B-Instruct-2507` * **TP Size:** 4 * **Engine:** V1 (TPU native JAX backend) ### Reproduction ```bash vllm serve Qwen/Qwen3-4B-Instruct-2507 \ --tensor-parallel-size 4 \ --dtype bfloat16 \ --enable-lora \ --max-lor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: orkspace/tpu_inference/tpu_inference/worker/tpu_worker.py", line 369, in compile_or_warm_up_model (EngineCore_DP0 pid=305) self.model_runner.capture_model() (EngineCore_DP0 pid=305) File "/workspace/tpu_inference/tpu_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: raph capture phase. ### Environment * **Hardware:** Cloud TPU v6e-4 (4 chips) * **vLLM Image:** `vllm/vllm-tpu:latest` (v0.13.0) * **Model:** `Qwen/Qwen3-4B-Instruct-2507` * **TP Size:** 4 * **Engine:** V1 (TPU native J...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
