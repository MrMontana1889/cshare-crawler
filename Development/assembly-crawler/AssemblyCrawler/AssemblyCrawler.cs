﻿// Crawler.cs
// Copyright (c) 2021 Kristopher L. Culin.  See LICENSE for details.

using System.Reflection;

namespace AssemblyCrawler
{
	public class AssemblyCrawler : IAssemblyCrawler
	{
		#region Constructor
		public AssemblyCrawler()
		{

		}
		#endregion

		#region Public Methods
		public void Crawl(Assembly assembly, IStubGenerator generator)
		{
			
		}
		#endregion
	}
}