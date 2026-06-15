# vllm-project/vllm#9713: [Usage]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. 

| 字段 | 值 |
| --- | --- |
| Issue | [#9713](https://github.com/vllm-project/vllm/issues/9713) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. 

### Issue 正文摘录

### Your current environment Error in using vllm ``` llm = LLM(model=os.path.join(cache_dir, finetuned_model_name), tensor_parallel_size=tensor_parallel_size) ``` The error details are ``` ERROR 10-26 11:35:32 registry.py:267] Error in inspecting model architecture 'LlamaForCausalLM' ERROR 10-26 11:35:32 registry.py:267] Traceback (most recent call last): ERROR 10-26 11:35:32 registry.py:267] File "D:\soft_install\anaconda3\envs\fuseAI\lib\site-packages\vllm\model_executor\models\registry.py", line 429, in _run_in_subprocess ERROR 10-26 11:35:32 registry.py:267] returned.check_returncode() ERROR 10-26 11:35:32 registry.py:267] File "D:\soft_install\anaconda3\envs\fuseAI\lib\subprocess.py", line 448, in check_returncode ERROR 10-26 11:35:32 registry.py:267] raise CalledProcessError(self.returncode, self.args, self.stdout, ERROR 10-26 11:35:32 registry.py:267] subprocess.CalledProcessError: Command '['D:\\soft_install\\anaconda3\\envs\\fuseAI\\python.exe', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1. ERROR 10-26 11:35:32 registry.py:267] ERROR 10-26 11:35:32 registry.py:267] The above exception was the direct cause of the following exception: ERROR...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [Usage]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. usage ### Your current environment Error in using vllm ``` llm = LLM(model=os.path.join(cache_dir, finetuned_model_name), tensor_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: recent call last): ERROR 10-26 11:35:32 registry.py:267] File "D:\soft_install\anaconda3\envs\fuseAI\lib\site-packages\vllm\model_executor\models\registry.py", line 429, in _run_in_subprocess ERROR 10-26 11:35:32 regist...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. usage ### Your current environment Error in using vllm ``` llm = LLM(model=os.path.join(cache_dir, finetuned_model_name), tensor_p...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: salLM', 'MambaForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'MiniCPM3ForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
