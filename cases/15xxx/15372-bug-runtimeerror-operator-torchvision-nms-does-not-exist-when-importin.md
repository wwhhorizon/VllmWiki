# vllm-project/vllm#15372: [Bug]: RuntimeError: operator torchvision::nms does not exist when importing vLLM (CPU Installation on Colab)

| 字段 | 值 |
| --- | --- |
| Issue | [#15372](https://github.com/vllm-project/vllm/issues/15372) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;import_error;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: operator torchvision::nms does not exist when importing vLLM (CPU Installation on Colab)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hey everyone, I tried installing vLLM on **Google Colab** following the CPU installation guidelines by running the following: ```bash !sudo apt-get update -y !sudo apt-get install -y gcc-12 g++-12 libnuma-dev !sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12 !git clone https://github.com/vllm-project/vllm.git vllm_source %cd vllm_source !pip install --upgrade pip !pip install "cmake>=3.26" wheel packaging ninja "setuptools-scm>=8" numpy !pip install -v -r requirements/cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu !VLLM_TARGET_DEVICE=cpu python setup.py install ``` When I `import vllm` I get the following RuntimeError: ```bash --------------------------------------------------------------------------- RuntimeError Traceback (most recent call last) /usr/local/lib/python3.11/dist-packages/transformers/utils/import_utils.py in _get_module(self, module_name) 1862 try: -> 1863 return importlib.import_module("." + module_name, self.__name__) 1864 except Exception as e: 31 frames RuntimeError: operator torchvision::nms does not exist The above exception was t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: RuntimeError: operator torchvision::nms does not exist when importing vLLM (CPU Installation on Colab) bug ### Your current environment ### 🐛 Describe the bug Hey everyone, I tried installing vLLM on **Google Col...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: speculative_decoding cuda;operator;triton build_error;crash;import_error;nondeterministic env_dependency;race_condition Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lp. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash;import_error;nondeterministic env_dependency;race_condition Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
