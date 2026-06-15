# vllm-project/vllm#9182: [Installation]: pip install vllm-0.6.2.zip err:setuptools-scm was unable to detect version for /tmp/pip-req-build-7ptioibj

| 字段 | 值 |
| --- | --- |
| Issue | [#9182](https://github.com/vllm-project/vllm/issues/9182) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: pip install vllm-0.6.2.zip err:setuptools-scm was unable to detect version for /tmp/pip-req-build-7ptioibj

### Issue 正文摘录

### Your current environment ```text pip install auto_gptq modelscope xformers==0.0.27.post2 torchvision==0.19 torchaudio torch==2.4.0 torchtext numpy wheel pip install setuptools>=74.1.1 setuptools_scm==8.1.0 pyportfolioopt pip install "pillow==10.*" -U pip install sentencepiece charset_normalizer cpm_kernels tiktoken -U pip install matplotlib scikit-learn tqdm tensorboard -U pip install datasets huggingface-hub transformers==4.45.0 -U pip install accelerate transformers_stream_generator -U pip install pydantic==1.7.4 typer==0.3.0 pip install fastrlock cupy-cuda11x==12.1.0 pip install vllm-flash-attn==2.6.1 datamodel_code_generator ``` ### How you are installing vllm ```sh pip install vllm-0.6.2.zip ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: pip install vllm-0.6.2.zip err:setuptools-scm was unable to detect version for /tmp/pip-req-build-7ptioibj installation ### Your current environment ```text pip install auto_gptq modelscope xformers==0.0.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r -U pip install pydantic==1.7.4 typer==0.3.0 pip install fastrlock cupy-cuda11x==12.1.0 pip install vllm-flash-attn==2.6.1 datamodel_code_generator ``` ### How you are installing vllm ```sh pip install vllm-0.6.2.zip `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: installation ### Your current environment ```text pip install auto_gptq modelscope xformers==0.0.27.post2 torchvision==0.19 torchaudio torch==2.4.0 torchtext numpy wheel pip install setuptools>=74.1.1 setuptools_scm==8....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
