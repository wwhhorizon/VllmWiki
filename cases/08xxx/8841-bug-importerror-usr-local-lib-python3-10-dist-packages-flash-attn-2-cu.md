# vllm-project/vllm#8841: [Bug]: ImportError: /usr/local/lib/python3.10/dist-packages/flash_attn_2_cuda.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

| 字段 | 值 |
| --- | --- |
| Issue | [#8841](https://github.com/vllm-project/vllm/issues/8841) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ImportError: /usr/local/lib/python3.10/dist-packages/flash_attn_2_cuda.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm is installed through below script ``` git clone https://github.com/vllm-project/vllm.git cd vllm git fetch --tags git checkout v0.6.2 pip install -e . ``` Loading `llama3.2-90b`(downloaded from [huggingface](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct)) ``` from vllm import LLM, SamplingParams llm = LLM( model="/models/llama3.2-90b", tensor_parallel_size=8, ) ``` The full error is here: https://gist.github.com/sfc-gh-zhwang/51bac374c35bb5c9dcaa4a0ef59d9fed ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: ImportError: /usr/local/lib/python3.10/dist-packages/flash_attn_2_cuda.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ringIcSt11char_traitsIcESaIcEEE bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm is installed through below script ``` git clone https://github.com/vllm-project/vllm.git c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: ImportError: /usr/local/lib/python3.10/dist-packages/flash_attn_2_cuda.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c105ErrorC2ENS_14SourceLocationENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;import_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;import_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
