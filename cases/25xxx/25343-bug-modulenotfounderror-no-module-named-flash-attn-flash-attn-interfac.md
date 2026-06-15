# vllm-project/vllm#25343: [Bug]:ModuleNotFoundError: No module named 'flash_attn.flash_attn_interface'

| 字段 | 值 |
| --- | --- |
| Issue | [#25343](https://github.com/vllm-project/vllm/issues/25343) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:ModuleNotFoundError: No module named 'flash_attn.flash_attn_interface'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Unable to start the qwen2.5vl-awq model ```python if __name__ == "__main__": from vllm import LLM, SamplingParams import os os.environ["CUDA_VISIBLE_DEVICES"] = "3" prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/home/dev/model/Qwen/Qwen2___5-VL-32B-Instruct-AWQ/") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ``` (EngineCore_DP0 pid=1531425) ERROR 09-21 22:46:24 [core.py:718] EngineCore failed to start. (EngineCore_DP0 pid=1531425) ERROR 09-21 22:46:24 [core.py:718] Traceback (most recent call last): (EngineCore_DP0 pid=1531425) ERROR 09-21 22:46:24 [core.py:718] File "/home/dev/liuyu/project/gpt_server/.venv/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 709, in run_engine_core (EngineCore_DP0 pid=1531425) ERROR 09-21 22:46:24 [core.py:718] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: qwen2.5vl-awq model ```python if __name__ == "__main__": from vllm import LLM, SamplingParams import os os.environ["CUDA_VISIBLE_DEVICES"] = "3" prompts = [ "Hello, my name is", "The president of the United States is",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Your current environment ### 🐛 Describe the bug Unable to start the qwen2.5vl-awq model ```python if __name__ == "__main__": from vllm import LLM, SamplingParams import os os.environ["CUDA_VISIBLE_DEVICES"] = "3" prompt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 09-21 22:46:24 [core.py:718] from . import attn_bias, ck, ck_splitk, cutlass, flash, flash3, triton_splitk (EngineCore_DP0 pid=1531425) ERROR 09-21 22:46:24 [core.py:718] File "/home/dev/liuyu/project/gpt_server/.venv/l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: from vllm import LLM, SamplingParams import os os.environ["CUDA_VISIBLE_DEVICES"] = "3" prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", ] sampling_params = SamplingP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: P0 pid=1531425) ERROR 09-21 22:46:24 [core.py:718] self.model_runner.profile_run() (EngineCore_DP0 pid=1531425) ERROR 09-21 22:46:24 [core.py:718] File "/home/dev/liuyu/project/gpt_server/.venv/lib/python3.11/site-packa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
