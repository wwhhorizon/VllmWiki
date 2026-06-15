# vllm-project/vllm#3528: ImportError: /usr/local/lib/python3.10/dist-packages/vllm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE

| 字段 | 值 |
| --- | --- |
| Issue | [#3528](https://github.com/vllm-project/vllm/issues/3528) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ImportError: /usr/local/lib/python3.10/dist-packages/vllm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE

### Issue 正文摘录

### Your current environment ```powershell accelerate 0.28.0 aiohttp 3.8.6 aiolimiter 1.1.0 aioprometheus 23.12.0 aiosignal 1.3.1 altair 5.1.2 annotated-types 0.6.0 antlr4-python3-runtime 4.9.3 anyio 3.7.1 async-timeout 4.0.3 attrs 23.1.0 auto_gptq 0.7.1 backoff 2.2.1 bce-python-sdk 0.8.95 beautifulsoup4 4.12.2 blinker 1.7.0 blis 0.7.11 Brotli 1.1.0 cachetools 5.3.2 catalogue 2.0.10 certifi 2023.7.22 cffi 1.16.0 chardet 5.2.0 charset-normalizer 3.3.2 click 8.1.7 cloudpathlib 0.16.0 cmake 3.27.7 coloredlogs 15.0.1 confection 0.1.3 contourpy 1.2.0 cryptography 41.0.5 cycler 0.12.1 cymem 2.0.8 dashscope 1.13.2 dataclasses 0.6 dataclasses-json 0.6.2 datasets 2.14.7 decorator 5.1.1 dill 0.3.7 distro 1.8.0 effdet 0.4.1 einops 0.7.0 emoji 2.8.0 et-xmlfile 1.1.0 exceptiongroup 1.1.3 faiss-cpu 1.7.4 fastapi 0.104.1 filelock 3.13.1 filetype 1.2.0 flatbuffers 23.5.26 fonttools 4.44.0 frozenlist 1.4.0 fschat 0.2.32 fsspec 2023.10.0 future 0.18.3 gekko 1.0.7 gitdb 4.0.11 GitPython 3.1.40 google 3.0.0 greenlet 3.0.1 h11 0.14.0 h2 4.1.0 hpack 4.0.0 httpcore 1.0.2 httptools 0.6.1 httpx 0.25.1 huggingface-hub 0.21.4 humanfriendly 10.0 hyperframe 6.0.1 idna 3.4 importlib-metadata 6.8.0 iniconfig 2....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ImportError: /usr/local/lib/python3.10/dist-packages/vllm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE installation;stale ### Your current environment ```powershell accelerate 0.28.0 aiohttp 3.8.6 aiolimiter 1.1.0 aioprometheus 23.12.0
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: gcodes 3.3.0 langdetect 1.0.9 langsmith 0.0.63 layoutparser 0.3.4 lit 17.0.4 lxml 4.9.3 Markdown 3.5.1 markdown-it-py 3.0.0 markdo
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE instal...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE installation...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
