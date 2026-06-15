# vllm-project/vllm#8461: [Bug]: Model architectures ['Qwen2AudioForConditionalGeneration'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#8461](https://github.com/vllm-project/vllm/issues/8461) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['Qwen2AudioForConditionalGeneration'] are not supported for now.

### Issue 正文摘录

### Your current environment pip install+https://github.com/vllm-project/vllm.git ### Model Input Dumps _No response_ ### 🐛 Describe the bug (VllmWorkerProcess pid=544861) ERROR 09-13 18:22:53 multiproc_worker_utils.py:226] File "/apps1/zhangfan/anaconda3/envs/new_swift/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 223, in _run_worker_process (VllmWorkerProcess pid=544861) ERROR 09-13 18:22:53 multiproc_worker_utils.py:226] output = executor(*args, **kwargs) (VllmWorkerProcess pid=544861) ERROR 09-13 18:22:53 multiproc_worker_utils.py:226] File "/apps1/zhangfan/anaconda3/envs/new_swift/lib/python3.10/site-packages/vllm/worker/worker.py", line 183, in load_model (VllmWorkerProcess pid=544861) ERROR 09-13 18:22:53 multiproc_worker_utils.py:226] self.model_runner.load_model() (VllmWorkerProcess pid=544861) ERROR 09-13 18:22:53 multiproc_worker_utils.py:226] File "/apps1/zhangfan/anaconda3/envs/new_swift/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 999, in load_model (VllmWorkerProcess pid=544861) ERROR 09-13 18:22:53 multiproc_worker_utils.py:226] self.model = get_model(model_config=self.model_config, (VllmWorkerProcess pid=544861) ERR...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Model architectures ['Qwen2AudioForConditionalGeneration'] are not supported for now. bug ### Your current environment pip install+https://github.com/vllm-project/vllm.git ### Model Input Dumps _No response_ ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ation'] are not supported for now. bug ### Your current environment pip install+https://github.com/vllm-project/vllm.git ### Model Input Dumps _No response_ ### 🐛 Describe the bug (VllmWorkerProcess pid=544861) ERROR 09...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Model architectures ['Qwen2AudioForConditionalGeneration'] are not supported for now. bug ### Your current environment pip install+https://github.com/vllm-project/vllm.git ### Model Input Dumps _No response_ ###...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: salLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalLM', 'OPTForCausalLM', 'O...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
