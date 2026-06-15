# vllm-project/vllm#9624: [Bug]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#9624](https://github.com/vllm-project/vllm/issues/9624) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now.

### Issue 正文摘录

### Your current environment ### Model Input Dumps python -O -u -m vllm.entrypoints.api_server \ --host=0.0.0.0 \ --port=8000 \ --model=/home/dandiago/models/Llama-2-13b-hf \ --served-model-name "Llama-2-13b-hf " \ --tensor-parallel-size=2 \ --distributed-executor-backend=ray ### 🐛 Describe the bug I use ray+vllm to serve Llama-2-13-hf. But failed. ERROR 10-23 23:20:26 registry.py:272] Error in inspecting model architecture 'LlamaForCausalLM' ERROR 10-23 23:20:26 registry.py:272] Traceback (most recent call last): ERROR 10-23 23:20:26 registry.py:272] File "/home/dandiago/anaconda3/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line 434, in _run_in_subprocess ERROR 10-23 23:20:26 registry.py:272] returned.check_returncode() ERROR 10-23 23:20:26 registry.py:272] File "/home/dandiago/anaconda3/lib/python3.12/subprocess.py", line 502, in check_returncode ERROR 10-23 23:20:26 registry.py:272] raise CalledProcessError(self.returncode, self.args, self.stdout, ERROR 10-23 23:20:26 registry.py:272] subprocess.CalledProcessError: Command '['/home/dandiago/anaconda3/envs/myenv/bin/python', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [Bug]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. bug ### Your current environment ### Model Input Dumps python -O -u -m vllm.entrypoints.api_server \ --host=0.0.0.0 \ --port=8000 \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /dandiago/anaconda3/envs/myenv/bin/python: Error while finding module specification for 'vllm.model_executor.models.registry' (ModuleNotFoundError: No module named 'vllm.model_executor') ERROR 10-23 23:20:26 registry.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. bug ### Your current environment ### Model Input Dumps python -O -u -m vllm.entrypoints.api_server \ --host=0.0.0.0 \ --port=8000 \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: a-2-13b-hf " \ --tensor-parallel-size=2 \ --distributed-executor-backend=ray ### 🐛 Describe the bug I use ray+vllm to serve Llama-2-13-hf. But failed. ERROR 10-23 23:20:26 registry.py:272] Error in inspecting model arch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
