# vllm-project/vllm#9712: [Doc]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#9712](https://github.com/vllm-project/vllm/issues/9712) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now.

### Issue 正文摘录

### 📚 The doc issue After I installed vllm, I got an error loading the model for inference ` llm = LLM(model=os.path.join(cache_dir, finetuned_model_name), tensor_parallel_size=tensor_parallel_size) ` The specific error is `J:\LM\cache_dir\WizardMath-7B-V1.0 ERROR 10-26 11:35:32 registry.py:267] Error in inspecting model architecture 'LlamaForCausalLM' ERROR 10-26 11:35:32 registry.py:267] Traceback (most recent call last): ERROR 10-26 11:35:32 registry.py:267] File "D:\soft_install\anaconda3\envs\fuseAI\lib\site-packages\vllm\model_executor\models\registry.py", line 429, in _run_in_subprocess ERROR 10-26 11:35:32 registry.py:267] returned.check_returncode() ERROR 10-26 11:35:32 registry.py:267] File "D:\soft_install\anaconda3\envs\fuseAI\lib\subprocess.py", line 448, in check_returncode ERROR 10-26 11:35:32 registry.py:267] raise CalledProcessError(self.returncode, self.args, self.stdout, ERROR 10-26 11:35:32 registry.py:267] subprocess.CalledProcessError: Command '['D:\\soft_install\\anaconda3\\envs\\fuseAI\\python.exe', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1. ERROR 10-26 11:35:32 registry.py:267] ERROR 10-26 11:35:32 registry.py:267] The a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: '] are not supported for now. documentation ### 📚 The doc issue After I installed vllm, I got an error loading the model for inference ` llm = LLM(model=os.path.join(cache_dir, finetuned_model_name), tensor_parallel_siz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Doc]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. documentation ### 📚 The doc issue After I installed vllm, I got an error loading the model for inference ` llm = LLM(model=os.path.j...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Doc]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. documentation ### 📚 The doc issue After I installed vllm, I got an error loading the model for inference ` llm = LLM(model=os.path.j...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
