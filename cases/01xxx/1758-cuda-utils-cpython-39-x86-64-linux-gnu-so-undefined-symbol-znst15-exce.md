# vllm-project/vllm#1758: cuda_utils.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZNSt15__exception_ptr13exception_ptr10_M_releaseEv

| 字段 | 值 |
| --- | --- |
| Issue | [#1758](https://github.com/vllm-project/vllm/issues/1758) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> cuda_utils.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZNSt15__exception_ptr13exception_ptr10_M_releaseEv

### Issue 正文摘录

Source code compilation error Command executed successfully： ``` git clone https://github.com/vllm-project/vllm.git cd vllm pip install -e . # This may take 5-10 minutes. ``` but: this error ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/home/sun/worker/models/gpt2-xl") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` error is: ``` /home/sun/anaconda3/envs/vllm_new/bin/python /home/sun/worker/vllm_test/vllm/bei_test.py Traceback (most recent call last): File "/home/sun/worker/vllm_test/vllm/bei_test.py", line 9, in from vllm import LLM, SamplingParams File "/home/sun/worker/vllm_test/vllm/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/home/sun/worker/vllm_test/vllm/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, ModelConfig, Paralle...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cuda_utils.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZNSt15__exception_ptr13exception_ptr10_M_releaseEv Source code compilation error Command executed successfully： ``` git clone https://github.com/vllm-project...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/home/sun/worker/models/gpt2-xl") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = outp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cuda_utils.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZNSt15__exception_ptr13exception_ptr10_M_releaseEv Source code compilation error Command executed successfully： ``` git clone https://github.com/vllm-project
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: : ``` /home/sun/anaconda3/envs/vllm_new/bin/python /home/sun/worker/vllm_test/vllm/bei_test.py Traceback (most recent call last): File "/home/sun/worker/vllm_test/vllm/bei_test.py", line 9, in from vllm import LLM, Samp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
